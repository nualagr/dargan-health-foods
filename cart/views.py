from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_cart(request):
    """
    A view that renders the shopping cart contents page.
    """
    return render(request, "cart/cart.html")


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

    # If product id already exists in the cart
    # Increment the quantity by the requested amount
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    # Put the cart variable in the session
    request.session["cart"] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """
    View to remove the specified item from the shopping cart.
    """
    cart = request.session.get("cart", {})

    if item_id in list(cart.keys()):
        cart.pop(item_id)

    request.session["cart"] = cart
    print(request.session["cart"])
    return redirect(reverse('view_cart'))


def increase_quantity_by_one(request, item_id):
    """
    View to increase the quantity of the
    specified item in the shopping cart by one.
    """
    cart = request.session.get('cart', {})
    if item_id in list(cart.keys()):
        cart[item_id] += 1

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def decrease_quantity_by_one(request, item_id):
    """
    View to decrease the quantity of the
    specified item in the shopping cart by one.
    """

    cart = request.session.get('cart', {})
    if item_id in list(cart.keys()):
        if cart[item_id] > 1:
            cart[item_id] -= 1
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
