from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, ProductTag, Category


def all_products(request):
    """
    A view to show all products,
    including sorting and search queriespytho
    """
    # Get all products from the database
    products = Product.objects.all()
    # So that we don't get an error when loading
    # the products page without the following terms.
    query = None
    categories = None
    department = None
    sort = None
    direction = None
    tag = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(
                    lower_name=Lower("name"))
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "department" in request.GET:
            department = request.GET["department"].split(",")
            all_categories = Category.objects.all()
            # Find a list of the names of the categories
            # associated with the department chosen
            department_categories = all_categories.filter(
                department__name__in=department).values_list(
                    'name', flat=True)
            products = products.filter(
                category__name__in=department_categories)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(
                name__in=categories).values_list(
                "name", flat=True)

        if "tag" in request.GET:
            tag = request.GET["tag"].split(",")
            product_tag_objects = ProductTag.objects.all()
            tagged_products = product_tag_objects.filter(tag__name__in=tag).values_list('product', flat=True)
            products = products.filter(id__in=tagged_products)

        if "q" in request.GET:
            query = request.GET["q"]
            # If the search was left blank
            if not query:
                messages.error(
                    request, "You did not enter any search criteria. Please try again.")
                return redirect(reverse("products"))

            queries = Q(
                name__icontains=query) | Q(information__icontains=query)
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_range = paginator.page_range

    context = {
            "products": products,
            "search_term": query,
            "current_department": department,
            "current_categories": categories,
            "current_tag": tag,
            "current_sorting": current_sorting,
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
