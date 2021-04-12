from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

from products.models import Product
from profiles.models import UserProfile

from .forms import ContactForm


def index(request):
    """ A view to return the index page. """
    # Get latest 4 products from the database
    latest_products = Product.objects.order_by("-date_added")[:4]
    context = {
        "latest_products": latest_products,
    }

    return render(request, "home/index.html", context)


def our_story(request):
    """ A view to render Our Story page. """
    return render(request, "home/our_story.html")


def contact(request):
    """
    A view to render the Contact Us page and form.
    If the user is logged in it prepopulates the form
    with their first name and email address.
    When the user submits a valid form the data is cleaned
    and an email containing the form data is sent to the
    site administrator.
    """
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
                    "Thanks for contacting us. A member of the Dargan Health Foods team will be in touch within 48 hours.",
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("contact")

    context = {
        "cform": form,
    }

    return render(request, "home/contact.html", context)
