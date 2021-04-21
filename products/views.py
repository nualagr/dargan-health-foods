from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum, Avg
from django.db.models.functions import Lower

from .models import Product, ProductTag, Category, Tag, ProductReview
from .forms import ProductForm, ProductAndTagsInlineFormSet, ProductReviewForm
from profiles.models import UserProfile


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
                    request, "No search criteria entered. Please try again."
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

    if "limit" in request.GET:
        # This request comes from the New In Dropdown
        # Find the limit submitted
        limit = request.GET["limit"].split(",")
        cap = limit[0]
        end_index = int(cap)
        # Slice the products list at the capped amount
        products = products[0:end_index]

    current_sorting = f"{sort}_{direction}"

    # Pagination
    paginator = Paginator(products, 12)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    page_range = paginator.page_range

    try:
        products_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products_list = paginator.page(paginator.num_pages)

    template = "products/products.html"
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

    return render(request, template, context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    """

    # Get the product from the database
    product = get_object_or_404(Product, pk=product_id)

    # Get the related product tags
    tags = ProductTag.objects.filter(product=product_id)

    # Get the related product reviews and order by latest added
    reviews = ProductReview.objects.filter(product=product_id).order_by(
        "-created"
    )

    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        # Get a list of the products purchased by the user
        products_purchased = user.orders.values_list(
            "lineitems__product", flat=True)
        # Get a list of the people who have reviewed the product already
        reviewers = reviews.values_list('user', flat=True)
        # If the current user has purchased the product
        # AND has not already reviewed it
        if (product_id in products_purchased and user.id not in reviewers):
            # Render the Leave a Review button
            can_review = True
        else:
            can_review = False
    else:
        # If the user is not logged in they cannot review a product
        can_review = False

    context = {
        "product": product,
        "tags": tags,
        "reviews": reviews,
        "can_review": can_review,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """
    View to aid the Super User to add a product to the store.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        # Instantiate a new instance of the ProductForm
        # Include request.FILES in order to make sure to
        # capture the image of the product if one was submitted
        pform = ProductForm(request.POST, request.FILES)
        ptformset = ProductAndTagsInlineFormSet(request.POST, request.FILES)

        if pform.is_valid():
            new_product = pform.save()
            # Find the new product id to add it to the product tags
            product_id = new_product.id
            product = get_object_or_404(Product, pk=product_id)
            ptformset = ProductAndTagsInlineFormSet(
                request.POST, request.FILES, instance=product
            )
            if ptformset.is_valid():
                for ptform in ptformset:
                    if ptform.is_valid():
                        if ptform.cleaned_data != {}:
                            ptform.save()
                messages.success(request, "Successfully added product!")
                return redirect(
                    reverse("product_detail", args=[new_product.id])
                )
        else:
            messages.error(
                request,
                "Failed to add product. Please ensure the form is valid.",
            )
    else:
        # If it was a GET request.
        # Create a blank product form
        pform = ProductForm()
        # Create a blank instance of the producttags inline formset
        ptformset = ProductAndTagsInlineFormSet()

    template = "products/add_product.html"
    context = {
        "pform": pform,
        "ptformset": ptformset,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    View to enable the Super User to edit existing products
    in the database.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    # Get the Product Object using the given id
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        # Create an instance of the product form using
        # that product's information
        pform = ProductForm(request.POST, request.FILES, instance=product)
        # Create an instance of the producttags inline formset
        ptformset = ProductAndTagsInlineFormSet(
            request.POST, request.FILES, instance=product
        )

        if pform.is_valid() and ptformset.is_valid():
            product = pform.save()
            ptformset.save()
            messages.success(request, "Successfully updated product!")
            # Redirect to the Product's Details Page
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product. Please ensure that the form is valid.",
            )

    else:
        # If the request is a GET request
        # Create an instance of the product form using the given product id
        pform = ProductForm(instance=product)
        # Create an instance of the producttags inline formset
        ptformset = ProductAndTagsInlineFormSet(instance=product)
        messages.info(request, f"You are editing {product.friendly_name}")

    template = "products/edit_product.html"
    context = {
        "pform": pform,
        "ptformset": ptformset,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    View to delete a product from the store.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))


@login_required
def add_review(request, product_id):
    """
    View to allow a logged_in user to add a product review to the site.
    """
    # Get the product from the database
    product = get_object_or_404(Product, pk=product_id)
    # Get the related product reviews and order by latest added
    reviews = ProductReview.objects.filter(product=product_id).order_by(
        "-created"
    )

    if request.method == "POST":
        # Get the current user
        user = UserProfile.objects.get(user=request.user)
        # Instantiate a new instance of the ProductReviewForm
        prform = ProductReviewForm(request.POST)

        if prform.is_valid():
            # Create Review object but don't save to database yet
            new_review = prform.save(commit=False)
            # Link the review to the product
            new_review.product = product
            # Link the logged-in user to the review
            new_review.user = user
            # Save the review to the database
            new_review.save()
            # Get the New Review Rating
            new_review_rating = new_review.review_rating
            # Work out the overall product rating
            if reviews:
                total_score = reviews.all().aggregate(
                    Sum('review_rating'))["review_rating__sum"]
                number_of_reviews = len(reviews) + 1
                avg_rating = (
                    total_score + new_review_rating) / number_of_reviews
            else:
                avg_rating = new_review_rating

            product.avg_rating = avg_rating
            product.save(update_fields=["avg_rating"])

            prform = ProductReviewForm()
            messages.success(request, "Successfully posted your review.")
            return redirect(reverse('product_detail', args=[product.id, ]))
        else:
            # If the form is invalid send an error message
            messages.error(
                request,
                "Failed to add review. Please ensure that the form is valid.",
            )

    else:
        # If it was a GET request
        # Instantiate a new instance of the Product Review Form
        prform = ProductReviewForm()

    context = {
        "prform": prform,
        "product": product,
    }

    return render(request, "products/add_review.html", context)


@login_required
def edit_review(request, review_id):
    """
    View to enable the logged-in User to edit
    their existing product review.
    """
    # Get the existing ProductReview object
    review = get_object_or_404(ProductReview, pk=review_id)
    # Get the product being reviewed
    product = get_object_or_404(Product, pk=review.product_id)

    if request.method == "POST":
        # Create an instance of the ProductReview form using
        # the posted data
        prform = ProductReviewForm(
            request.POST, instance=review)

        if prform.is_valid():

            prform.save()
            rating = prform.cleaned_data['review_rating']
            # Update average rating for the product
            reviews = ProductReview.objects.filter(product=product)
            avg_rating = reviews.aggregate(
                Avg('review_rating'))['review_rating__avg']
            if avg_rating:
                product.avg_rating = int(avg_rating)
            # If all reviews for this product have been deleted
            # set the average to zero
            else:
                product.avg_rating = 0

            product.save(update_fields=["avg_rating"])

            messages.success(request, "Successfully updated your review!")
            # Redirect to the Product's Details Page
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update your review. Please ensure that the form is valid.",
            )

    else:
        # Populate the ProductReview form
        # with the existing review from the database
        prform = ProductReviewForm(instance=review)
        # If the request is a GET request
        messages.info(
            request,
            f"You are editing your review of { product.friendly_name }")

    template = "products/edit_review.html"
    context = {
        "prform": prform,
        "product": product,
        "review": review,
    }
    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """
    View to enable logged-in users to delete their own product reviews.
    """
    # Get the ProductReview and the Product
    review = get_object_or_404(ProductReview, pk=review_id)
    product = get_object_or_404(Product, pk=review.product_id)

    # Delete the review and return a success message
    try:
        review.delete()

        # Update average rating for the product
        reviews = ProductReview.objects.filter(product=product)
        avg_rating = reviews.aggregate(
            Avg('review_rating'))['review_rating__avg']
        if avg_rating:
            product.avg_rating = int(avg_rating)
        # If all reviews for this product have been deleted
        # set the average to zero
        else:
            product.avg_rating = 0

        product.save()

        messages.success(request, 'Your review was deleted')

    # If the review was not deleted return an error message
    except Exception as e:
        messages.error(request, "We couldn't delete your review because "
                                f" error:{e} occured. Please try again later.")

    return redirect(reverse('product_detail', args=(product.id,)))
