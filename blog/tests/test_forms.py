from django.test import TestCase
from ..forms import BlogPostForm, BlogPostCommentForm


class TestBlogPostForm(TestCase):
    def test_valid_form(self):
        """
        Test BlogPostForm validation.
        """
        form = BlogPostForm(
            {
                "title": "Blog Post Test title",
                "subtitle": "Blog Post Test subtitle",
                "intro": "Blog Post Test introduction",
                "content": "Blog Post Test content",
            }
        )
        self.assertTrue(form.is_valid())


class TestBlogPostCommentForm(TestCase):
    def test_valid_form(self):
        """
        Test BlogPostCommentForm validation.
        """
        form = BlogPostCommentForm({"content": "This is a test comment."})
        self.assertTrue(form.is_valid())

    def test_content_is_required(self):
        """
        Test that the Content field within the
        BlogPostCommentForm is required.
        """
        form = BlogPostCommentForm({"content": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("content", form.errors.keys())
        self.assertEqual(form.errors["content"][0], "This field is required.")
