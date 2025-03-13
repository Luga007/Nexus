from django.shortcuts import render
from category.models import Category, Region, Brand
from product.models import Product, ProductImage, ProductView
from django.db.models import Count
from django.db.models import Prefetch

# Create your views here.

def main(request):
    categories = Category.objects.filter(is_main =True)
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_image'))
    region = Region.objects.all()
    ctx = {
        'categories': categories,
        'products': products,
        'region': region
    }
    return render(request, 'index-2.html', ctx)

