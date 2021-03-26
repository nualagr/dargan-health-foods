from django.shortcuts import render, redirect

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
    # Increment the quantity
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    # Put the cart variable in the session
    request.session["cart"] = cart
    print(request.session["cart"])
    return redirect(redirect_url)
