from django.contrib import admin
from .models import Order, OrderLineItem

# Admin Models code taken from the Code Institute
# Boutique Ado walkthrough project and then modified


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "order_number",
        "date",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_cart",
        "stripe_pid",
    )

    fields = (
        "order_number",
        "user_profile",
        "date",
        "full_name",
        "email",
        "phone_number",
        "billing_street_address1",
        "billing_street_address2",
        "billing_town_or_city",
        "billing_county",
        "billing_postcode",
        "billing_country",
        "shipping_street_address1",
        "shipping_street_address2",
        "shipping_town_or_city",
        "shipping_county",
        "shipping_postcode",
        "shipping_country",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_cart",
        "stripe_pid",
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "order_total",
        "delivery_cost",
        "grand_total",
    )

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
