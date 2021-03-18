from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    A view to show all products,
    including sorting and search queries
    """
    # Get all products from the database
    products = Product.objects.all()
    print("Products:", products)

    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_range = paginator.page_range

    context = {
            "products": products,
            "page_obj": page_obj,
            "page_range": page_range,
        }

    return render(request, "products/products.html", context)
