from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page. """

    return render(request, 'home/index.html')


def our_story(request):
    """ A view to render Our Story page. """
    return render(request, 'home/our_story.html')
