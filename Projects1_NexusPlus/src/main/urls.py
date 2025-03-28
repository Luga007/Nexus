from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('service/', views.services, name='service'),
    path('contact/', views.contact, name='contact'),
]