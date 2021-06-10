from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Product
from profiles.models import UserProfile, DiscountCode2User
from cart.models import DiscountCode

from decimal import Decimal


def cart_contents(request):

    cart_items = []
    total = 0
    total_before_discount = 0
    product_count = 0
    discount_code_object = None
    discount_amount = 0

    # Get the cart if it exists or initialize it to an empty dict if not
    cart = request.session.get("cart", {})
    # Iterate through all the items in the cart
    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        if product.on_offer and product.discount_price:
            total += quantity * product.discount_price
        else:
            total += quantity * product.price
        product_count += quantity
        cart_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "product": product,
            }
        )
    # If the user is logged in, then check discount
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        discount = request.session.get("discount", {})

        if discount:
            # Check to see whether the DiscountCode2User for this user exists
            discount_code_object = DiscountCode.objects.filter(
                pk=discount["discount_code_id"]
            ).first()
            user_discount_code = DiscountCode2User.objects.filter(
                discount_code=discount_code_object, user=user
            ).first()

            # Check if the discount exists
            # if not delete it from the user's session
            # (Condensing of 'if' statements suggested by Mr. Reuben Ferrante)
            if (
                discount_code_object and
                user_discount_code and
                user_discount_code.active
            ):
                total_before_discount = total
                # Calculate the discount to be applied
                percentage_discount = discount_code_object.percentage_discount
                discount_amount = total * Decimal(percentage_discount)
                total -= discount_amount
            else:
                del request.session["discount"]

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        "cart_items": cart_items,
        "discount_amount": discount_amount,
        "discount_code": discount_code_object,
        "total_before_discount": total_before_discount,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
