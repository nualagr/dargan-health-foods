from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
    require_GET,
)
from products.models import Product
from .models import DiscountCode
from .forms import DiscountCodeForm
from profiles.models import UserProfile, DiscountCode2User


@require_http_methods(["GET", "POST"])
def view_cart(request):
    """
    A view that renders the shopping cart contents page
    and the empty DiscountCodeForm.
    When posting from this view, the discount code, if valid,
    is added to the session cookie so that it can be accessed
    by the cart_contents function in the context.py file.
    """
    discount = request.session.get("discount", {})
    discount_code_form = DiscountCodeForm()

    if request.method == "POST":
        discount_code_form = DiscountCodeForm(request.POST)
        if discount_code_form.is_valid():
            discount_code = discount_code_form.cleaned_data["discount_code"]
            if request.user.is_authenticated:
                user = get_object_or_404(UserProfile, user=request.user)
                try:
                    # Get the code from the database or set variable to None
                    discount_code_object = DiscountCode.objects.filter(
                        discount_code=discount_code
                    ).first()
                    # Get the DiscountCode2User object or set variable to None
                    discount_code_2_user = DiscountCode2User.objects.filter(
                        discount_code=discount_code_object, user=user
                    ).first()
                    # If the DiscountCode2User object exists & is still active
                    if discount_code_2_user and discount_code_2_user.active:
                        discount["discount_code_id"] = discount_code_object.id
                        # Put the promocode id variable in the session
                        # so that the discount can be applied in the
                        # cart_contents context
                        request.session["discount"] = discount
                        messages.success(
                            request,
                            "Promo Code applied.",
                        )
                        return redirect(reverse("view_cart"))
                    # If the DiscountCode2User object exists
                    # but is no longer active
                    elif discount_code_2_user:
                        messages.error(
                            request,
                            "Promo Code no longer active.",
                        )
                        return redirect(reverse("view_cart"))
                    # The DiscountCode2User object does not exist
                    else:
                        messages.error(
                            request,
                            "Promo Code not recognised.",
                        )
                        return redirect(reverse("view_cart"))
                except DiscountCode.DoesNotExist:
                    messages.error(
                        request,
                        ("Promo Code not recognised."),
                    )
                    # Return the user to the Shopping Cart page
                    return redirect(reverse("view_cart"))
        else:
            discount_code_form = DiscountCodeForm()
            # Add a message to the request object
            messages.error(
                request,
                "There was an error applying the discount. \
                Please double check your code.",
            )

    template = "cart/cart.html"
    context = {
        "dcform": discount_code_form,
    }
    return render(request, template, context)


@require_POST
def add_to_cart(request, item_id):
    """
    Add a quantity of the specified product to the shopping cart.
    """
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    # Create a variable called cart
    # If it already exists get the variable
    # Else set it to an empty dict
    cart = request.session.get("cart", {})
    # Get the product to be added
    product = Product.objects.get(pk=item_id)

    # If product id already exists in the cart
    # Increment the quantity by the requested amount
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request,
            f"Added another {product.friendly_name} to your cart.",
        )
    else:
        cart[item_id] = quantity
        # Add a message to the request object
        messages.success(
            request, f"Added {product.friendly_name} to your cart"
        )

    # Put the cart variable in the session
    request.session["cart"] = cart
    return redirect(redirect_url)


@require_POST
def remove_from_cart(request, item_id):
    """
    View to remove the specified item from the shopping cart
    and alert the user as to whether the action was successful
    or not. If this empties the cart completely, check whether
    a discount code had been applied. If so, remove from the
    session cookie.
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get("cart", {})

        if item_id in list(cart.keys()):
            cart.pop(item_id)
            # If the cart is now empty
            if not cart:
                # Check if a discount code had been applied
                if "discount" in request.session:
                    # Remove the unused Discount Code from the Session
                    del request.session["discount"]
            messages.success(
                request,
                f"Removed {product.friendly_name} from your shopping cart.",
            )

        request.session["cart"] = cart
        return redirect(reverse("view_cart"))

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return redirect(reverse("view_cart"))


@require_POST
def increase_quantity_by_one(request, item_id):
    """
    View to increase the quantity of the
    specified item in the shopping cart by one.
    """
    try:
        cart = request.session.get("cart", {})

        if item_id in list(cart.keys()):
            cart[item_id] += 1
            messages.success(
                request,
                "Cart updated.",
            )

        request.session["cart"] = cart
        return redirect(reverse("view_cart"))

    except Exception as e:
        messages.error(request, f"Error updating item quantity: {e}")
        return redirect(reverse("view_cart"))


@require_POST
def decrease_quantity_by_one(request, item_id):
    """
    View to decrease the quantity of the
    specified item in the shopping cart by one.
    If this empties the cart, check whether a
    discount code had been applied. If so,
    delete it from the session cookie.
    """

    cart = request.session.get("cart", {})
    product = get_object_or_404(Product, pk=item_id)

    if item_id in list(cart.keys()):
        if cart[item_id] > 1:
            cart[item_id] -= 1
            messages.success(
                request,
                "Cart updated.",
            )
        else:
            cart.pop(item_id)
            # If the cart is now empty
            if not cart:
                # Check if a discount code had been applied
                if "discount" in request.session:
                    # Remove the unused Discount Code from the Session
                    del request.session["discount"]
            messages.success(
                request,
                f"Removed {product.friendly_name} from your shopping cart.",
            )

    request.session["cart"] = cart
    return redirect(reverse("view_cart"))


@login_required
@require_GET
def remove_discount_code(request):
    """
    View to remove the discount code that had been applied
    to the cart total by deleting the 'discount' variable from
    the session cookie.
    """

    # Remove the Discount Code from the Session
    if "discount" in request.session:
        del request.session["discount"]
        messages.success(
            request,
            "Promo Code removed.",
        )

    return redirect(reverse("view_cart"))
