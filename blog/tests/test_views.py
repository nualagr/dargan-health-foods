from django.test import TestCase
from blog.models import BlogPost


class TestBlogViews(TestCase):
    def test_all_posts_view(self):
        """
        Test for status code 200 response and correct
        template rendered when getting the blog page.
        """
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog.html")

    def test_individual_blog_post_view(self):
        """
        Test for status code 200 response and correct
        template rendered when getting an individual blog_post page.
        """
        blogpost = BlogPost.objects.create(title="My test blogpost")
        blogpost.save()
        response = self.client.get("/blog/blog_post/{0}/".format(
            blogpost.slug))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog_post.html")
