from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_posts, name='blog'),
    path('blog_post/<slug:slug>/', views.blog_post, name='blog_post'),
]
