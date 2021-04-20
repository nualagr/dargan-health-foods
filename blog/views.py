from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import BlogPost
from .forms import BlogPostForm
from profiles.models import UserProfile


def all_posts(request):
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
    """ A view to return individual blog post page """

    blogpost = get_object_or_404(BlogPost, slug=slug)

    template = "blog/blog_post.html"
    context = {
        "blogpost": blogpost,
    }

    return render(request, template, context)


@login_required
def add_post(request):
    """
    A view to render the BlogPost Form for Super Users.
    Upload submitted BlogPost forms to the database.
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
        user = get_object_or_404(UserProfile, user=request.user)

        if bpform.is_valid():
            # Create Blog object but don't save to database yet
            new_post = bpform.save(commit=False)
            # Assign the author to the new blog and save it
            new_post.author = user
            new_post.save()
            slug = new_post.slug
            messages.success(
                request, 'Successfully uploaded your new blog post.')
            return redirect(
                    reverse("blog_post", args=[slug])
                )
        else:
            messages.error(request, 'Failed to add the new blog post. \
                           Please ensure that the form is valid.')

    # If the request is a GET request create a new blank form
    # for the SuperUser to input the new blog post
    bpform = BlogPostForm()
    template = "blog/add_post.html"

    context = {
        "bpform": bpform,
    }

    return render(request, template, context)


@login_required
def delete_post(request, blogpost_id):
    """
    View to delete a blog post from the Blog.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only Dargan team members can do that.")
        return redirect(reverse("blog"))

    blogpost = get_object_or_404(BlogPost, id=blogpost_id)
    blogpost.delete()
    messages.success(request, "BlogPost successfully deleted!")
    return redirect(reverse("blog"))
