from django.shortcuts import render
from . import models
from django.db.models import Prefetch

def products(request):
    products = models.Product.objects.prefetch_related(
        Prefetch('images', queryset=models.ProductImage.objects.filter(is_main=True), to_attr='main_image'))
    ctx = {
        'products': products
    }
    return render(request, 'product.html', ctx)
