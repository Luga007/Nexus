from django.shortcuts import render
from category.models import Category, Region, Brand
from product.models import Product, ProductImage


# Create your views here.

def category(request):
    product = Product.objects.all()
    productImage = ProductImage.objects.filter(is_main=True)
    category = Category.objects.filter(is_main=True)
    region = Region.objects.all()
    brand = Brand.objects.all()
    ctx = {
           'product': product,
           'category': category,
           'region': region,
           'brand': brand,
           'product_image': productImage
           }
    return render(request, 'category.html', ctx)