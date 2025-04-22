from django.shortcuts import render, redirect
from . import models
from django.db.models import Prefetch
from user.models import Profile
from category.models import Category
from django.db.models import Count, Sum
from django.core.paginator import Paginator
from .forms import ProductForm
from django.contrib.auth import authenticate, login, logout

def products(request):
    page = request.GET.get('page', 1)
    products = models.Product.objects.prefetch_related(
        Prefetch('images', queryset=models.ProductImage.objects.filter(is_main=True), to_attr='main_image')
    ).order_by('-created_at')
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


def product_add(request, name, pk):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)

            if request.user.is_authenticated:
                if not hasattr(request.user, 'profile'):
                    Profile.objects.create(user=request.user)

                product.user = request.user.profile
                product.save()
                return redirect('main')
    else:
        form = ProductForm()

    product = models.Product.objects.select_related('user').all()
    category = Category.objects.filter(is_main=True)

    advertisement = models.Product.objects.all()
    # product1 = models.Product.objects.filter(name=name, pk=pk)
    # product1.delete()

    ctx = {
        'forms': form,
        'categories': category,
        'users': product,
        'advertisement': advertisement,
    }
    return render(request, 'post-ads.html', ctx)

def logout_view(request):
   logout(request)
   return redirect('main')


def dashboard(request):
    return render(request, 'dashboard.html', {})