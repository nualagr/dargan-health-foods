from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse,
)
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
    require_GET,
)
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from cart.models import DiscountCode

from products.models import Product
from profiles.models import UserProfile, DiscountCode2User
from profiles.forms import UserProfileForm
from cart.contexts import cart_contents

import stripe
import json
import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Before calling the confirmCardPayment() method in Stripe JS
# Make a POST request to this view and pass it the
# client_secret from the paymentIntent.
# This way we can post to the view from JS and if everything
# goes OK we should get a 200 response.
@require_POST
def cache_checkout_data(request):
    try:
        # Split the client_secret at the word 'secret'.
        # The first part will be the paymentIntent ID
        pid = request.POST.get("client_secret").split("_secret")[0]
        save_data = request.POST.get("save_info")
        # Set up Stripe with the secret key so the
        # paymentIntent can be modified.
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "cart": json.dumps(request.session.get("cart", {})),
                "save_info": save_data,
                "username": request.user,
                "discount": json.dumps(request.session.get("discount", {})),
            },
        )
        return HttpResponse(status=200)
    # If anything goes wrong, add a message and return the
    # status for a bad request.
    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be \
            processed right now. Please try again later.",
        )
        return HttpResponse(content=e, status=400)


@require_http_methods(["GET", "POST"])
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        # The user is trying to submit their payment details
        cart = request.session.get("cart", {})
        # Get the discount code if one exists
        discount = request.session.get("discount", {})

        # Create a dict with the data from the Billing Details form
        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "town_or_city": request.POST["town_or_city"],
            "county": request.POST["county"],
            "country": request.POST["country"],
            "postcode": request.POST["postcode"],
        }

        # Create an instance of the form from the form data
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # Create the Order but don't save to the database just yet
            order = order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            if discount:
                order.discount_code = DiscountCode.objects.get(
                    pk=discount["discount_code_id"]
                )
            # Now save the Order to the database
            order.save()
            logger.info(f"Order {pid} saved to the database.")
            # Iterate through the cart to create each OrderLineItem
            for item_id, quantity in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        (
                            "One of the products in your \
                            shopping cart wasn't found in our database. \
                            Please call us for assistance!"
                        ),
                    )
                    # Delete the empty order
                    order.delete()
                    # Return the user to the Shopping Cart page
                    return redirect(reverse("view_cart"))
            # Save the info to the user's profile if all is well
            request.session["save_info"] = "save-info" in request.POST
            return redirect(
                reverse("checkout_success", args=[order.order_number])
            )
        # If order form is not valid
        else:
            messages.error(
                request,
                "There was an error with your form. \
                Please double check your information.",
            )

    # GET request
    else:
        cart = request.session.get("cart", {})
        if not cart:
            messages.error(
                request, "There's nothing in your shopping cart at the moment."
            )
            return redirect(reverse("products"))

        # Get the contents of the cart from the dict
        # that was added to the request context
        current_cart = cart_contents(request)
        total = current_cart["grand_total"]
        # Convert the grand total from a decimal to an integer for Stripe
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the Order Form with any info
        # the user maintains in their Profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(
                    initial={
                        "full_name": profile.user.get_full_name(),
                        "email": profile.user.email,  # From the User Account
                        "phone_number": profile.default_phone_number,
                        "street_address1": profile.default_street_address1,
                        "street_address2": profile.default_street_address2,
                        "town_or_city": profile.default_town_or_city,
                        "county": profile.default_county,
                        "country": profile.default_country,
                        "postcode": profile.default_postcode,
                    }
                )
            # If the User does not have saved info in their account
            except UserProfile.DoesNotExist:
                order_form = OrderForm()

        else:
            order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(
                request,
                "Stripe public key is missing. \
                Did you forget to set it in your environment?",
            )

        template = "checkout/checkout.html"
        context = {
            "order_form": order_form,
            "stripe_public_key": stripe_public_key,
            "client_secret": intent.client_secret,
        }

        return render(request, template, context)


@require_GET
def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        username = profile.user.username
        # Attach the user's profile to the Order
        order.user_profile = profile
        order.save()
        pid = order.stripe_pid
        logger.info(f"{username}s profile attached to Order {pid}.")

        # If a discount code was used, deactivate it
        if order.discount_code:
            discount = order.discount_code
            discount_code_object = get_object_or_404(
                DiscountCode, discount_code=discount.discount_code
            )
            discount_code_2_user = DiscountCode2User.objects.get(
                user=profile, discount_code=discount_code_object
            )
            discount_code_2_user.active = False
            discount_code_2_user.save()

        # Save the user's info if the box was checked
        if save_info is True:
            profile_data = {
                # These dict keys match the fields on the user profile model
                "default_phone_number": order.phone_number,
                "default_street_address1": order.street_address1,
                "default_street_address2": order.street_address2,
                "default_town_or_city": order.town_or_city,
                "default_county": order.county,
                "default_country": order.country,
                "default_postcode": order.postcode,
            }
            # Create an instance of the User Profile Form using the data
            # and update the Profile we obtained above
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()
            logger.info(f"{username}s default profile info has been updated")

    messages.success(
        request,
        f"Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.",
    )

    # Empty the Shopping Cart
    if "cart" in request.session:
        del request.session["cart"]

    # Remove the used Discount Code from the Session
    if "discount" in request.session:
        del request.session["discount"]

    template = "checkout/checkout_success.html"
    context = {
        # Send the order back to the template
        "order": order,
    }

    return render(request, template, context)
