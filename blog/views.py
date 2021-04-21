from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import BlogPost, BlogPostTag
from .forms import BlogPostForm, BlogPostAndTagsInlineFormSet
from profiles.models import UserProfile


def all_posts(request):
    """
    A view to fetch all the blog posts in the database
    ordered by date descending.
    Send the list of posts to the blog.html page.
    """
    # Get all the BlogPosts from the database, in descending order by date
    blogs_list = BlogPost.objects.all().order_by("-created_on")
    total_post_count = blogs_list.count()
    paginator = Paginator(blogs_list, 4)  # 4 posts maximum on each page
    page = request.GET.get('page')
    try:
        blogs_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        blogs_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        blogs_list = paginator.page(paginator.num_pages)

    template = "blog/blog.html"
    context = {
        "blog_page": "active",
        "page": page,
        "blogs_list": blogs_list,
        "total_post_count": total_post_count,
    }

    return render(request, template, context)


def blog_post(request, slug):
    """
    A view to return an individual Blog Post page.
    """
    # Get the specified BlogPost from the database
    blogpost = get_object_or_404(BlogPost, slug=slug)
    # Get the related BlogPostTag objects
    tags = BlogPostTag.objects.filter(blogpost=blogpost.id)

    template = "blog/blog_post.html"
    context = {
        "blogpost": blogpost,
        "tags": tags,
    }

    return render(request, template, context)


@login_required
def add_post(request):
    """
    A view to render an empty BlogPost Form and BlogPostTags Formset
    for Super Users.
    On submit, once forms are deemed valid, create BlogPost and BlogPostTag
    objects and upload them to the database.
    """
    if not request.user.is_superuser:
        messages.error(
            request, "Sorry, only Dargan staff members have access to this.")
        return redirect(reverse("home"))

    if request.method == 'POST':
        # Instantiate a new instance of the BlogPostForm
        # Include request.FILES in order to make sure to
        # capture the image if one was submitted
        bpform = BlogPostForm(request.POST, request.FILES)
        bptformset = BlogPostAndTagsInlineFormSet(request.POST, request.FILES)
        user = get_object_or_404(UserProfile, user=request.user)

        if bpform.is_valid():
            # Create BlogPost object but don't save it to the database yet
            new_post = bpform.save(commit=False)
            # Assign the User as Author to the new BlogPost and save it
            new_post.author = user
            new_post.save()
            slug = new_post.slug
            # Find the new BlogPost id to add it to the blogpost tag objects
            blogpost_id = new_post.id
            blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
            bptformset = BlogPostAndTagsInlineFormSet(
                request.POST, request.FILES, instance=blogpost
            )
            # Save each individual BlogPostTag object
            if bptformset.is_valid():
                for bptform in bptformset:
                    if bptform.is_valid():
                        if bptform.cleaned_data != {}:
                            bptform.save()
            messages.success(
                request, 'Successfully uploaded your new blog post.')
            return redirect(
                    reverse("blog_post", args=[slug])
                )
        else:
            messages.error(request, 'Failed to add the new blog post. \
                           Please ensure that the form is valid.')

    # If the request is a GET request create a new blank BlogPost form
    # to enable the SuperUser to input a new blog post
    bpform = BlogPostForm()
    # Create a blank instance of the blogposttags inline formset
    bptformset = BlogPostAndTagsInlineFormSet()
    template = "blog/add_post.html"

    context = {
        "bpform": bpform,
        "bptformset": bptformset,
    }

    return render(request, template, context)


@login_required
def edit_post(request, blogpost_id):
    """
    View to enable the Super User to edit existing blog posts
    and their associated tags in the database.
    """
    if not request.user.is_superuser:
        messages.error(
            request, "Sorry, only members of the Dargan Team can do that.")
        return redirect(reverse("blog"))

    # Get the BlogPost Object using the given id
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    if request.method == "POST":
        # Create an instance of the BlogPost form using
        # the given post's existing data from the database.
        bpform = BlogPostForm(request.POST, request.FILES, instance=blogpost)
        # Create an instance of the blogposttags inline formset
        bptformset = BlogPostAndTagsInlineFormSet(
            request.POST, request.FILES, instance=blogpost
        )

        if bpform.is_valid() and bptformset.is_valid():
            blogpost = bpform.save()
            bptformset.save()
            messages.success(request, "Successfully updated blog post!")
            # Redirect to the BlogPost's Page using the Slug
            return redirect(reverse("blog_post", args=[blogpost.slug]))
        else:
            messages.error(
                request,
                "Failed to update blog post. Please ensure that the form is valid.",
            )

    else:
        # If the request is a GET request
        # Create an instance of the BlogPost form using the given post id
        bpform = BlogPostForm(instance=blogpost)
        # Create an instance of the producttags inline formset
        bptformset = BlogPostAndTagsInlineFormSet(instance=blogpost)
        messages.info(
            request, f"You are editing blog post: { blogpost.title }")

    template = "blog/edit_post.html"
    context = {
        "bpform": bpform,
        "bptformset": bptformset,
        "blogpost": blogpost,
    }

    return render(request, template, context)


@login_required
def delete_post(request, blogpost_id):
    """
    View to delete a blog post from the database.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only Dargan team members can do that.")
        return redirect(reverse("blog"))

    blogpost = get_object_or_404(BlogPost, id=blogpost_id)
    # Solution to removing the related, now redundant, image
    # from the Media folder found on Stack Overflow:
    # https://stackoverflow.com/questions/56205957/django-delete-file-after-filefield-delete
    blogpost.main_image.close()
    blogpost.main_image.delete()
    blogpost.delete()
    messages.success(request, "BlogPost successfully deleted!")
    return redirect(reverse("blog"))
