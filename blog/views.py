from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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
