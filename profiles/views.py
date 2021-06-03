from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET

from .models import UserProfile
from .forms import UserProfileForm
from blog.models import BlogPostComment
from checkout.models import Order
from products.models import ProductReview


@login_required
@require_http_methods(["GET", "POST"])
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
                request, "Update failed. Please ensure your form is valid."
            )
    else:
        form = UserProfileForm(instance=user)

    my_reviews = (
        ProductReview.objects.all().filter(user=user).order_by("-created")
    )
    my_comments = (
        BlogPostComment.objects.all().filter(user=user).order_by("-created_on")
    )
    my_orders = user.orders.all().order_by("-date")

    template = "profiles/profile.html"
    context = {
        "form": form,
        "orders": my_orders,
        "reviews": my_reviews,
        "comments": my_comments,
        "on_profile_page": True,
    }

    return render(request, template, context)


@login_required
@require_GET
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number \
                {order_number}. \
                    A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)
