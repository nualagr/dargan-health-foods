from django.test import TestCase
from django.template.defaultfilters import slugify
from blog.models import Topic, BlogPost, BlogPostComment


class TestBlogPostModels(TestCase):

    def test_topic_creation(self):
        """
        Test that BlogPost Topics are created using the Topic
        model and that they return the correct name.
        """
        topic = Topic.objects.create(
            name="testtopic",
            friendly_name="Test Topic",
        )
        topic.save()
        self.assertTrue(isinstance(topic, Topic))
        self.assertEqual("testtopic", topic.name)

    def test_blogpost_creation(self):
        """
        Test whether BlogPosts are created using the BlogPost model.
        Test whether the BlogPost title is returned correctly.
        """
        blogpost = BlogPost.objects.create(title="My test blogpost")
        blogpost.save()
        self.assertTrue(isinstance(blogpost, BlogPost))
        self.assertEqual("My test blogpost", blogpost.title)

    def test_blogpost_has_slug(self):
        """
        Test whether BlogPosts slugs are correctly created
        from the BlogPost title when the BlogPost is saved.
        """
        blogpost = BlogPost.objects.create(title="My test post")
        blogpost.save()
        self.assertEqual(blogpost.slug, slugify(blogpost.title))

    def test_blogpostcomment_creation(self):
        """
        Test whether BlogPostComments are created using the correct model.
        Test whether the comment is connected to the related blogpost.
        """
        blogpost = BlogPost.objects.create(title="My test blogpost")
        blogpost.save()
        blogpostcomment = BlogPostComment.objects.create(
            blogpost=blogpost,
        )
        blogpostcomment.save()
        self.assertTrue(isinstance(blogpostcomment, BlogPostComment))
        self.assertEqual("My test blogpost", blogpostcomment.blogpost.title)
