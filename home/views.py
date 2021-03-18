from django.shortcuts import render
from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the index page. """
    # Get latest 4 products from the database
    latest_products = Product.objects.order_by('-date_added')[:4]
    print("Latest Products:", latest_products)
    context = {
        "latest_products": latest_products,
        }

    return render(request, 'home/index.html', context)


def our_story(request):
    """ A view to render Our Story page. """
    return render(request, 'home/our_story.html')
