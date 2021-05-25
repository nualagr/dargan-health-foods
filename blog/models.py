from django.db import models
from django.template.defaultfilters import slugify

from profiles.models import UserProfile
from products.models import Tag


class Topic(models.Model):
    """
    Creates a Topic model containing the names of
    blog post topics.
    """

    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class BlogPost(models.Model):
    topic = models.ForeignKey(
        Topic,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="blogposttopic",
    )
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    intro = models.TextField()
    content = models.TextField()
    main_image = models.ImageField(
        upload_to="blog_images", null=True, blank=True
    )
    created_on = models.DateField(auto_now_add=True, editable=False)
    author = models.ForeignKey(
        UserProfile,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="usersblogposts",
    )
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)


class BlogPostTag(models.Model):
    blogpost = models.ForeignKey(
        BlogPost,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="taggedblogposts",
    )
    tag = models.ForeignKey(
        Tag,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="blogposttags",
    )

    def __str__(self):
        return "{}, {}".format(self.blogpost, self.tag.friendly_name)


class BlogPostComment(models.Model):
    blogpost = models.ForeignKey(
        BlogPost,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="blogpostcomments",
    )
    user = models.ForeignKey(
        UserProfile,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="usersblogpostcomments",
    )
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return "{}, {}".format(self.blogpost, self.user)
