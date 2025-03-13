from django.shortcuts import render
from product.models import Product, ProductImage
from django.db.models import Prefetch
from user.models import Profile
def details(request):
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_image'))
    # user = Product.objects.select_related('user').all()
    user = Profile.objects.all()
    ctx = {
        'products': products,
        'users': user
    }
    return render(request, 'details.html', ctx)
