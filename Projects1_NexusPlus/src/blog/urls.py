from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<int:pk>', views.post_list, name='post'),
]