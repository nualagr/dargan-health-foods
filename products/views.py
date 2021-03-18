from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductTag


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


def product_detail(request, product_id):
    """
    A view to show individual product details
    """
    # Get the product from the database
    product = get_object_or_404(Product, pk=product_id)

    # Get the related product tags
    tags = ProductTag.objects.filter(product=product_id)
    print("Tags:", tags)
    context = {
        "product": product,
        "tags": tags,
    }

    return render(request, "products/product_detail.html", context)
