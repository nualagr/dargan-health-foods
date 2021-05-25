from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_cart, name="view_cart"),
    path("add/<item_id>/", views.add_to_cart, name="add_to_cart"),
    path(
        "increase_quantity/<item_id>/",
        views.increase_quantity_by_one,
        name="increase_quantity_by_one",
    ),
    path(
        "decrease_quantity/<item_id>/",
        views.decrease_quantity_by_one,
        name="decrease_quantity_by_one",
    ),
    path("remove/<item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path(
        "remove_discount_code",
        views.remove_discount_code,
        name="remove_discount_code",
    ),
]
