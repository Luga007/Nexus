from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.products, name='product'),
    path('details/<int:pk>', views.details, name='details'),
    path('product-add', views.product_add, name='product-add'),
    path('dashboard', views.dashboard, name='dashboard'),
]