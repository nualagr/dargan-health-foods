from django.contrib import admin
from .models import NewsletterSubscription


class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "email_address",
        "date_subscribed",
    )
    readonly_fields = (
        "pk",
        "email_address",
        "date_subscribed",
    )
    ordering = ("-date_subscribed",)


admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)
