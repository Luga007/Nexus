from django.shortcuts import render
from category.models import Category, Region, Brand
from product.models import Product, ProductImage
from django.db.models import Prefetch


# Create your views here.

def category_views(request):
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_image'))
    category = Category.objects.filter(is_main=True)
    region = Region.objects.all()
    brand = Brand.objects.all()
    ctx = {
           'products': products,
           'category': category,
           'region': region,
           'brand': brand,
           }
    return render(request, 'category.html', ctx)