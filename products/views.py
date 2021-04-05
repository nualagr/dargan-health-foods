from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, ProductTag, Category, Tag
from .forms import ProductForm


def all_products(request):
    """
    A view to show all products,
    including sorting and search queries
    """
    # Get all products from the database
    products = Product.objects.all()
    # Get all product tag objects from the database
    product_tag_objects = ProductTag.objects.all()
    # So that we don't get an error when loading
    # the products page without the following terms.
    query = None
    category = None
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
                products = products.annotate(lower_name=Lower("name"))
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
                department__name__in=department
            ).values_list("name", flat=True)
            products = products.filter(
                category__name__in=department_categories
            )

        if "category" in request.GET:
            category = request.GET["category"].split(",")
            products = products.filter(category__name__in=category)
            category = Category.objects.filter(name__in=category).values_list(
                "name", flat=True
            )

        if "tag" in request.GET:
            tag = request.GET["tag"].split(",")
            tagged_products = product_tag_objects.filter(
                tag__name__in=tag
            ).values_list("product", flat=True)
            products = products.filter(id__in=tagged_products)

        if "q" in request.GET:
            query = request.GET["q"]
            # If the search was left blank
            if not query:
                messages.error(
                    request,
                    "No search criteria entered. Please try again."
                )
                return redirect(reverse("products"))

            all_tags = Tag.objects.all().values_list("name", flat=True)
            # Check to see if the search term is a Tag
            if all_tags.filter(friendly_name__iexact=query):
                tagged_products = product_tag_objects.filter(
                    tag__friendly_name__iexact=query
                ).values_list("product", flat=True)
                products = products.filter(id__in=tagged_products)
            # If not a recognized tag, search the following
            # product table fields for the search term
            else:
                queries = (
                    Q(name__icontains=query)
                    | Q(information__icontains=query)
                    | Q(ingredients__icontains=query)
                    | Q(category__name__icontains=query)
                    | Q(brand__name__icontains=query)
                )
                products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    # Pagination
    paginator = Paginator(products, 4)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    page_range = paginator.page_range

    try:
        products_list = paginator.page(page)
    except PageNotAnInteger:
        products_list = paginator.page(1)
    except EmptyPage:
        products_list = paginator.page(paginator.num_pages)

    context = {
        "products": products_list,
        "search_term": query,
        "current_department": department,
        "current_category": category,
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

    context = {
        "product": product,
        "tags": tags,
    }

    return render(request, "products/product_detail.html", context)


def add_product(request):
    """
    View to aid the Super User to add a product to the store.
    """
    if request.method == "POST":
        # Instantiate a new instance of the ProductForm
        # Include request.FILES in order to make sure to
        # capture the image of the product if one was submitted
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("add_product"))
        else:
            messages.error(
                request,
                "Failed to add product. Please ensure the form is valid.")
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """
    A view to Edit an existing product.
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(request, "Failed to update product. Please ensure that the form is valid.", )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.friendly_name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)
