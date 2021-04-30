from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product
from .models import DiscountCode
from .forms import DiscountCodeForm


def view_cart(request):
    """
    A view that renders the shopping cart contents page
    and the empty DiscountCodeForm.
    """
    discount = request.session.get("discount", {})
    discount_code_form = DiscountCodeForm()

    if request.method == "POST":
        discount_code_form = DiscountCodeForm(request.POST)
        if discount_code_form.is_valid():
            discount_code = discount_code_form.cleaned_data["discount_code"]
            print("This is the code that was entered:", discount_code)
            try:
                # Get the code from the database
                discount_code_object = DiscountCode.objects.get(
                    discount_code=discount_code)
                print("This is the discount_code_object", discount_code_object)
                if discount_code_object:
                    discount["discount_code_id"] = discount_code_object.id
                    percentage_discount = discount_code_object.percentage_discount
                    print("This is the percentage discount to be applied:",
                          percentage_discount)
                    # Put the promocode variable in the session
                    request.session["discount"] = discount
                    return redirect(reverse("view_cart"))
            except DiscountCode.DoesNotExist:
                messages.error(
                        request,
                        (
                            "Promo Code not recognised."
                        ),
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
        messages.success(request, f"Added {product.friendly_name} to your cart")

    # Put the cart variable in the session
    request.session["cart"] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """
    View to remove the specified item from the shopping cart
    and alert the user as to whether the action was successful
    or not.
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get("cart", {})

        if item_id in list(cart.keys()):
            cart.pop(item_id)
            messages.success(
                request,
                f"Removed {product.friendly_name} from your shopping cart.",
            )

        request.session["cart"] = cart
        print(request.session["cart"])
        return redirect(reverse("view_cart"))

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return redirect(reverse("view_cart"))


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
        messages.error(request, f"Error updating item quanity: {e}")
        return redirect(reverse("view_cart"))


def decrease_quantity_by_one(request, item_id):
    """
    View to decrease the quantity of the
    specified item in the shopping cart by one.
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
            messages.success(
                request,
                f"Removed {product.friendly_name} from your shopping cart.",
            )

    request.session["cart"] = cart
    return redirect(reverse("view_cart"))
