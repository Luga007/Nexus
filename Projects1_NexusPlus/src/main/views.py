from django.shortcuts import render

from category.models import Category, Region, Brand
from product.models import Product, ProductImage, ProductView



# Create your views here.

def main(request):
    categories = Category.objects.filter(is_main =True)
    product = Product.objects.all()
    productImage = ProductImage.objects.filter(is_main =True)
    region = Region.objects.all()
    ctx = {
        'categories': categories,
        'product': product,
        'product_image': productImage,
        'region': region
    }
    return render(request, 'index-2.html', ctx)