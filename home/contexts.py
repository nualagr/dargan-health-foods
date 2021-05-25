from .forms import NewsletterSubscriptionForm


def newsletter_subscription_form(request):
    sub_form = NewsletterSubscriptionForm()
    context = {"newsletter_subscription_form": sub_form}
    return context
