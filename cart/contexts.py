from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from cart.models import DiscountCode


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
        cart_items.append({
            "item_id": item_id,
            "quantity": quantity,
            "product": product,
        })

    discount = request.session.get("discount", {})
    print("This is the discount printing from contexts.py", discount)

    if discount:
        total_before_discount = total
        print(
            "This is the discount code id printing from contexts.py",
            discount["discount_code_id"])
        discount_code_object = get_object_or_404(
            DiscountCode, pk=discount["discount_code_id"])
        percentage_discount = discount_code_object.percentage_discount
        discount_amount = total * Decimal(percentage_discount / 100)
        total -= discount_amount

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
