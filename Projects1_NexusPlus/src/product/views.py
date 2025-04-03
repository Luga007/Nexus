from django.shortcuts import render, redirect
from . import models
from django.db.models import Prefetch
from user.models import Profile
from category.models import Category
from django.db.models import Count, Sum
from django.core.paginator import Paginator
from .forms import ProductForm

def products(request):
    page = request.GET.get('page', 1)
    products = models.Product.objects.prefetch_related(
        Prefetch('images', queryset=models.ProductImage.objects.filter(is_main=True), to_attr='main_image'))
    categories = Category.objects.filter(parent=None).annotate(count_pr=Count('product'))
    paginator = Paginator(products, 2)
    page_obj = paginator.get_page(page)

    ctx = {
        'products': products,
        'categories': categories,
        'page_obj': page_obj,
        'countOfProducts': page,
    }
    return render(request, 'product.html', ctx)


def details(request, pk):
    product = (
        models.Product.objects
        .select_related('category', 'location', 'brand', 'user')
        .prefetch_related('images')
        .get(pk=pk)
    )
    posted_by = models.Profile.objects.get(pk=product.user.pk)
    products_by_seller = (
        models.Product.objects
        .filter(user=product.user)
        .select_related('location', 'brand', 'user')
        .prefetch_related(Prefetch('images', queryset=models.ProductImage.objects.filter(is_main=True)))
    )

    ctx = {
        "product": product,
        "posted_by": posted_by,
        "products_by_seller": products_by_seller,


    }
    return render(request, 'details.html', ctx)

def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            products = form.save(commit=False)
            print('USER', request.user.profile)
            products.user = request.user.profile
            return render('main')
    else:
        form = ProductForm()

    product = models.Product.objects.select_related('user').all()
    category = Category.objects.filter(is_main=True)
    ctx = {
        'forms': form,
        'categories': category,
        'users': product,
    }
    return render(request, 'post-ads.html', ctx)