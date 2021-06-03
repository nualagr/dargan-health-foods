from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from products.models import Tag
from .models import BlogPost, BlogPostTag, BlogPostComment, Topic
from .forms import (
    BlogPostForm,
    BlogPostAndTagsInlineFormSet,
    BlogPostCommentForm,
)
from profiles.models import UserProfile


def all_posts(request):
    """
    A view to fetch all the blog posts in the database
    including topic, tag and search queries.
    """
    # Get all the BlogPosts from the database, in descending order by date
    blogs_list = BlogPost.objects.all().order_by("-created_on")
    total_post_count = blogs_list.count()
    # Get all BlogPostTags from the database
    blogposttags = BlogPostTag.objects.all()
    # So that we don't get an error when loading
    # the blog page without the following terms.
    blogquery = None
    topic = None
    tag = None

    if request.GET:

        if "topic" in request.GET:
            topic = request.GET["topic"].split(",")
            blogs_list = blogs_list.filter(topic__name__in=topic)
            topic = Topic.objects.filter(name__in=topic).values_list(
                "name", flat=True
            )

        if "tag" in request.GET:
            tag = request.GET["tag"].split(",")
            tagged_posts = blogposttags.filter(tag__name__in=tag).values_list(
                "blogpost", flat=True
            )
            blogs_list = blogs_list.filter(id__in=tagged_posts)

        if "bq" in request.GET:
            blogquery = request.GET["bq"]
            # If the search was left blank
            if not blogquery:
                messages.error(
                    request, "No search criteria entered. Please try again."
                )
                return redirect(reverse("blog"))

            all_tags = Tag.objects.all().values_list("name", flat=True)
            # Check to see if the search term is a Tag
            if all_tags.filter(friendly_name__iexact=blogquery):
                tagged_posts = blogposttags.filter(
                    tag__friendly_name__iexact=blogquery
                ).values_list("blogpost", flat=True)
                blogs_list = blogs_list.filter(id__in=tagged_posts)
            # If not a recognized tag, search the following
            # blogpost fields for the search term
            else:
                queries = (
                    Q(title__icontains=blogquery) |
                    Q(subtitle__icontains=blogquery) |
                    Q(intro__icontains=blogquery) |
                    Q(content__icontains=blogquery) |
                    Q(topic__name__icontains=blogquery)
                )
                blogs_list = blogs_list.filter(queries)

    # Pagination
    paginator = Paginator(blogs_list, 4)  # 4 posts maximum on each page
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    page_range = paginator.page_range

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
        "page_obj": page_obj,
        "page_range": page_range,
        "blogs_list": blogs_list,
        "blog_search_term": blogquery,
        "total_post_count": total_post_count,
        "current_blog_topic": topic,
        "current_blog_tag": tag,
    }

    return render(request, template, context)


def blog_post(request, slug):
    """
    A view to return an individual Blog Post page
    and the associated comments from the database.
    If the user is logged in, render an empty comment form.
    """
    # Get the specified BlogPost from the database
    blogpost = get_object_or_404(BlogPost, slug=slug)
    # Get the related BlogPostTag objects
    tags = BlogPostTag.objects.filter(blogpost=blogpost.id)
    # Get the related BlogPostComment objects
    comments = BlogPostComment.objects.filter(blogpost=blogpost.id)

    if request.user.is_authenticated:
        try:
            user = UserProfile.objects.get(user=request.user)
            bpcform = BlogPostCommentForm()
        except UserProfile.DoesNotExist:
            bpcform = BlogPostCommentForm(
                initial={"user": user, "blogpost": blogpost}
            )
    else:
        bpcform = BlogPostCommentForm()

    template = "blog/blog_post.html"
    context = {
        "blogpost": blogpost,
        "tags": tags,
        "comments": comments,
        "bpcform": bpcform,
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
            request, "Sorry, only Dargan staff members have access to this."
        )
        return redirect(reverse("home"))

    if request.method == "POST":
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
                request, "Successfully uploaded your new blog post."
            )
            return redirect(reverse("blog_post", args=[slug]))
        else:
            messages.error(
                request,
                "Failed to add the new blog post. \
                           Please ensure that the form is valid.",
            )

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
            request, "Sorry, only members of the Dargan Team can do that."
        )
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
                "Failed to update blog post. \
                           Please ensure that the form is valid.",
            )

    else:
        # If the request is a GET request
        # Create an instance of the BlogPost form using the given post id
        bpform = BlogPostForm(instance=blogpost)
        # Create an instance of the producttags inline formset
        bptformset = BlogPostAndTagsInlineFormSet(instance=blogpost)
        messages.info(
            request, f"You are editing blog post: { blogpost.title }"
        )

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


@login_required
def add_comment(request, blogpost_id):
    """
    View to allow a logged-in user to add a comment to
    a post on the Dargan Blog.
    """
    # Get the blogpost from the database
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    # Get the current user
    user = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        # Instantiate a new instance of the BlogPostCommentForm
        bpcform = BlogPostCommentForm(request.POST)

        if bpcform.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = bpcform.save(commit=False)
            # Link the comment to the blogpost
            new_comment.blogpost = blogpost
            # Link the logged-in user to the comment
            new_comment.user = user
            # Save the review to the database
            new_comment.save()

            bpcform = BlogPostCommentForm()
            messages.success(request, "Successfully posted your comment.")
            return redirect(
                reverse(
                    "blog_post",
                    args=[
                        blogpost.slug,
                    ],
                )
            )
        else:
            # If the form is invalid send an error message
            messages.error(
                request,
                "Failed to add comment. Please ensure that the form is valid.",
            )
    else:
        # If it was a GET request
        # Instantiate a new instance of the Blog Post Comment Form
        bpcform = BlogPostCommentForm()

    template = "blog/add_comment.html"
    context = {
        "bpcform": bpcform,
        "blogpost": blogpost,
    }

    return render(request, template, context)


@login_required
def edit_comment(request, blogpostcomment_id):
    """
    View to enable the logged-in User to edit
    their existing blogpost comments.
    The referring url is captured and if the
    user accessed this view from their profile
    page they are redirected there after submission.
    """
    # Get the existing BlogPostComment object
    blogpostcomment = get_object_or_404(BlogPostComment, pk=blogpostcomment_id)
    # Get the blog post being commented on
    blogpost = get_object_or_404(BlogPost, pk=blogpostcomment.blogpost.pk)

    if request.method == "POST":
        # Create an instance of the BlogPostCommentForm using
        # the posted data
        bpcform = BlogPostCommentForm(request.POST, instance=blogpostcomment)

        if bpcform.is_valid():
            bpcform.save()
            # Get the previous page url from the hidden form input
            previous_page_url = request.POST.get("previous_page_url")
            messages.success(request, "Successfully updated your comment!")
            # If the user got to the edit comment page from their profile
            # Redirect them back to their profile page.
            if "profile" in previous_page_url:
                return redirect(reverse("profile"))
            else:
                # Redirect to the related blog_post.html page
                return redirect(reverse("blog_post", args=[blogpost.slug]))
        else:
            messages.error(
                request,
                "Failed to update your comment. \
                    Please ensure that the form is valid.",
            )

    else:
        # Populate the BlogPostComment form
        # with the existing content from the database
        bpcform = BlogPostCommentForm(instance=blogpostcomment)
        # If the request is a GET request
        messages.info(
            request,
            f"You are editing your comment on the blog post \
                { blogpost.title }",
        )

    template = "blog/edit_comment.html"
    context = {
        "bpcform": bpcform,
        "blogpost": blogpost,
        "blogpostcomment": blogpostcomment,
    }
    return render(request, template, context)


@login_required
def delete_comment(request, blogpostcomment_id):
    """
    View to enable logged-in users to delete their own
    blog post comments.
    """
    # Get the BlogPostComment and the BlogPost
    blogpostcomment = get_object_or_404(BlogPostComment, pk=blogpostcomment_id)
    blogpost = get_object_or_404(BlogPost, pk=blogpostcomment.blogpost.id)

    # Delete the comment and return a success message
    try:
        blogpostcomment.delete()

        messages.success(request, "Your comment was deleted")

    # If the comment was not deleted return an error message
    except Exception as e:
        messages.error(
            request,
            "We couldn't delete your comment because "
            f" error:{e} occurred. Please try again later.",
        )

    return redirect(reverse("blog_post", args=(blogpost.slug,)))
