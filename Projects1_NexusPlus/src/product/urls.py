from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.products, name='product'),
    path('details/<int:pk>', views.details, name='details')
]