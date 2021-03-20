from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, ProductTag


def all_products(request):
    """
    A view to show all products,
    including sorting and search queries
    """
    # Get all products from the database
    products = Product.objects.all()
    print("Products:", products)
    # So that we don't get an error when loading
    # the products page without a search term.
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            # If the search was left blank
            if not query:
                messages.error(
                    request, "You did not enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(information__icontains=query)
            products = products.filter(queries)

    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_range = paginator.page_range

    context = {
            "products": products,
            "search_term": query,
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
