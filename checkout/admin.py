from django.contrib import admin
from .models import Order, OrderLineItem

# Admin Model OrderAdmin and OrderLineItemAdminInline
# taken initially from the Code Institute
# Boutique Ado walkthrough project and then modified


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("product_price_paid", "lineitem_total",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline, )

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
        "street_address1",
        "street_address2",
        "town_or_city",
        "county",
        "postcode",
        "country",
        "discount_code",
        "discount_amount",
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
