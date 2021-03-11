from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('our_story/', views.our_story, name='our_story'),
]
