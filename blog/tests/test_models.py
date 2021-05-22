from django.test import TestCase
from django.template.defaultfilters import slugify
from ..models import Topic, BlogPost, BlogPostComment, BlogPostTag
from products.models import Tag


class TestBlogPostModels(TestCase):
    def create_topic(
        self,
        name="testtopic",
        friendly_name="Test Topic",
    ):
        """
        Function to create a Topic for testing purposes.
        """
        return Topic.objects.create(
            name=name, friendly_name=friendly_name
        )

    def create_blogpost(
        self,
        title="My Test BlogPost",
    ):
        """
        Function to create a BlogPost for testing purposes.
        """
        return BlogPost.objects.create(
            title=title
        )

    def test_topic_creation(self):
        """
        Test that Topics are created using the Topic
        model.
        """
        t = self.create_topic()
        self.assertTrue(isinstance(t, Topic))

    def test_topic_string_method(self):
        """
        Test that Topics return the correct string.
        """
        t = self.create_topic()
        self.assertEqual(str(t), "testtopic")

    def test_topic_get_friendly_name_method(self):
        """
        Test that Topics return the correct friendly name.
        """
        t = self.create_topic()
        self.assertEqual(t.get_friendly_name(), "Test Topic")

    def test_blogposttag_string_method(self):
        """
        Test that BlogPostTags return a formatted string
        containing the related blogpost title as well as
        the tag friendly name.
        """
        tag = Tag.objects.create(friendly_name="Test Tag")
        bp = self.create_blogpost()
        blogposttag = BlogPostTag.objects.create(blogpost=bp, tag=tag)
        self.assertEqual(str(blogposttag), "My Test BlogPost, Test Tag")

    def test_blogpost_creation(self):
        """
        Test whether BlogPosts are created using the BlogPost model.
        Test whether the BlogPost title is returned correctly.
        """
        bp = self.create_blogpost()
        self.assertTrue(isinstance(bp, BlogPost))
        self.assertEqual("My Test BlogPost", bp.title)

    def test_blogpost_string_method(self):
        """
        Test that BlogPosts return the correct string.
        """
        bp = self.create_blogpost()
        self.assertEqual(str(bp), "My Test BlogPost")

    def test_blogpost_has_slug(self):
        """
        Test whether BlogPosts slugs are created
        from the BlogPost title when the BlogPost is saved.
        """
        bp = self.create_blogpost()
        self.assertEqual(bp.slug, slugify(bp.title))

    def test_blogpostcomment_creation(self):
        """
        Test whether BlogPostComments are created using the correct model.
        Test whether the comment is connected to the related blogpost.
        """
        bp = self.create_blogpost()
        blogpostcomment = BlogPostComment.objects.create(
            blogpost=bp,
        )
        blogpostcomment.save()
        self.assertTrue(isinstance(blogpostcomment, BlogPostComment))
        self.assertEqual("My Test BlogPost", blogpostcomment.blogpost.title)
