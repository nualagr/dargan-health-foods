from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views.decorators.http import (
    require_http_methods,
    require_GET,
    require_POST,
)
from django.contrib import messages

from products.models import Product
from profiles.models import UserProfile
from blog.models import BlogPost
from .models import NewsletterSubscription
from .forms import NewsletterSubscriptionForm, ContactForm

import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)


@require_GET
def index(request):
    """
    A view to find the four most recently added products
    and the two most recent blog posts in the database.
    Render the index.html template using that data.
    """
    # Get latest 4 products from the database
    latest_products = Product.objects.order_by("-date_added")[:4]
    # Get latest 2 blogposts from the database
    latest_posts = BlogPost.objects.order_by("-created_on")[:2]
    context = {
        "latest_products": latest_products,
        "latest_posts": latest_posts,
    }

    return render(request, "home/index.html", context)


@require_GET
def our_story(request):
    """ A view to render Our Story page. """
    return render(request, "home/our_story.html")


@require_http_methods(["GET", "POST"])
def contact(request):
    """
    A view to render the Contact Us page and form.
    If the user is logged in it prepopulates the form
    with their first name and email address.
    When the user submits a valid form the data is cleaned
    and an email containing the form data is sent to the
    site administrator.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            from_name = form.cleaned_data["your_name"]
            from_email = form.cleaned_data["your_email"]
            message = form.cleaned_data["your_message"]
            subject = "Dargan Health Foods Enquiry"
            try:
                send_mail(
                    subject,
                    f"Customer Query From: {from_name}\
                         \n Message: \n {message}\
                         \n Contact me at: {from_email}",
                    from_email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                messages.success(
                    request,
                    "Thanks for contacting us. \
                        A member of the Dargan Health Foods \
                            team will be in touch within 48 hours.",
                )
                logger.info(f"Customer Query from {from_email} sent.")
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("contact")

    # If it was a GET request
    if request.user.is_authenticated:
        # If the user is logged in, prepopulate the form
        try:
            profile = UserProfile.objects.get(user=request.user)
            form = ContactForm(
                initial={
                    "your_name": profile.user.first_name,
                    "your_email": profile.user.email,
                }
            )
        except UserProfile.DoesNotExist:
            form = ContactForm()
    else:
        # If the user is not logged in, create a blank form
        form = ContactForm()

    context = {
        "cform": form,
    }

    return render(request, "home/contact.html", context)


@require_POST
def subscribe(request):
    """
    A view to get the email address from the Newsletter
    Subscription Form when submitted.
    Check whether the address already exists in the database.
    If so, send message and redirect to the same page.
    If not, add the email to the database and send a success
    message to the User.
    """
    newsletter_subscription_form = NewsletterSubscriptionForm()
    subscribe_redirect = request.POST.get("subscribe_redirect")

    newsletter_subscription_form = NewsletterSubscriptionForm(request.POST)
    if NewsletterSubscription.objects.filter(
        email_address=request.POST.get("email_address")
    ).exists():
        messages.info(request, "You are already subscribed to our newsletter.")
        return redirect(subscribe_redirect)
    else:
        if newsletter_subscription_form.is_valid():
            email_address = request.POST.get("email_address")
            newsletter_subscription_form.save()
            messages.success(
                request, "You are now subscribed to our newsletter."
            )
            logger.info(f"{email_address} subscribed to Newsletter.")
        else:
            messages.error(
                request,
                "Failed to submit request. Please ensure \
                that the form is valid.",
            )
    return redirect(subscribe_redirect)
