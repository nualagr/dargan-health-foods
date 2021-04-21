from django.contrib import admin
from .models import BlogPost, Topic


class TopicAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "friendly_name",
        "name",
    )

    ordering = ('friendly_name',)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "topic",
        "slug",
        "created_on",
    )
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Topic, TopicAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
