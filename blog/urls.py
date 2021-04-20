from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_posts, name='blog'),
    path('blog_post/<slug:slug>/', views.blog_post, name='blog_post'),
    path('add_post/', views.add_post, name='add_post'),
]
