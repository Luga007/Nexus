from django.shortcuts import render
from category.models import Category, Region, Brand
from product.models import Product, ProductImage, ProductView
from django.db.models import Count
from django.db.models import Prefetch
from user.models import Profile
from blog.models import Blog

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

def about(request):
    products = Product.objects.annotate()
    user_c = Profile.objects.aggregate(userc=Count('first_name'))
    product_c = Category.objects.aggregate(productc=Count('product'))
    product_l = Product.objects.aggregate(locationc=Count('location'))
    blog_c = Profile.objects.aggregate(blogc=Count('blog'))
    ctx = {
        'user_count': user_c,
        'product_count': product_c,
        'location_count': product_l,
        'blog_count': blog_c
    }
    return render(request, 'about.html', ctx)

def services(request):
    user_c = Profile.objects.aggregate(userc=Count('first_name'))
    product_c = Category.objects.aggregate(productc=Count('product'))
    product_l = Product.objects.aggregate(locationc=Count('location'))
    blog_c = Profile.objects.aggregate(blogc=Count('blog'))
    ctx = {
        'user_count': user_c,
        'product_count': product_c,
        'location_count': product_l,
        'blog_count': blog_c,
    }
    return render(request, 'services.html', ctx)

def contact(request):
    ctx = {

    }
    return render(request, 'contact.html', ctx)


def login(request):
    ctx = {

    }
    return render(request, 'login.html', ctx)

def register(request):
    ctx = {

    }
    return render(request, 'register.html', ctx)