from django.shortcuts import render


def profile(request):
    """
    View to display a User's Profile Page
    where they can access their default 
    shipping information and order history.
    """
    template = "profiles/profile.html"
    context = {}

    return render(request, template, context)
