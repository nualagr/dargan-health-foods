from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from blog.models import BlogPostComment
from checkout.models import Order
from products.models import ProductReview


@login_required
def profile(request):
    """
    View to display a User's Profile Page
    where they can access their default
    shipping information and order history.
    """
    user = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
        else:
            messages.error(
                request, "Update failed. Please ensure your form is valid.")
    else:
        form = UserProfileForm(instance=user)

    my_reviews = ProductReview.objects.all().filter(
        user=user).order_by("-created")
    my_comments = BlogPostComment.objects.all().filter(
        user=user).order_by("-created_on")
    orders = user.orders.all().order_by("-date")
    template = "profiles/profile.html"
    context = {
        "form": form,
        "orders": orders,
        "reviews": my_reviews,
        "comments": my_comments,
        "on_profile_page": True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)
