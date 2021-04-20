from django.db import models
from django.template.defaultfilters import slugify

from profiles.models import UserProfile
from products.models import Tag


class Topic(models.Model):
    """
    Creates a Topic model containing the names of
    blog post topics
    """

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class BlogPost(models.Model):
    topic = models.CharField(max_length=200)
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
    tags = models.ForeignKey(
        Tag,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="tags",
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    # def delete(self, using=None, keep_parents=False):
    #     self.blogpost.storage.delete(self.pk)
    #     self.main_image.storage.delete(self.pk)
    #     super().delete()
