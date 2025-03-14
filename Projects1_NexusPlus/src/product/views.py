from django.shortcuts import render
from . import models
from django.db.models import Prefetch
from user.models import Profile

def products(request):
    products = models.Product.objects.prefetch_related(
        Prefetch('images', queryset=models.ProductImage.objects.filter(is_main=True), to_attr='main_image'))
    ctx = {
        'products': products,
    }
    return render(request, 'product.html', ctx)


# def details(request, pk):
#     products = models.Product.objects.prefetch_related(
#         Prefetch('images', queryset=models.ProductImage.objects.filter(is_main=True), to_attr='main_image'))
#     ctx = {
#         'products': products,
#     }
#     return render(request, 'details.html', ctx)


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