from django.contrib import admin
from .models import (
    Department,
    Category,
    Brand,
    Tag,
    Product,
    ProductImage,
    ProductTag,
)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "friendly_name",
        "name",
    )

    ordering = ('friendly_name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "friendly_name",
        "name",
        "department",
    )

    ordering = ('friendly_name',)


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "friendly_name",
        "name",
    )

    ordering = ('friendly_name',)


class TagAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "friendly_name",
        "name",
    )

    ordering = ("friendly_name",)


class ProductTagInline(admin.TabularInline):
    model = ProductTag


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = (
        ProductTagInline,
        ProductImageInline,
    )

    list_display = (
        "pk",
        "sku",
        "friendly_name",
        "brand",
        "size_value",
        "size_unit",
        "price",
        "free_from",
        "category",
        "date_added",
        "num_in_stock",
        "discontinued",
    )

    ordering = ("sku",)


# Register your models here.
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)
