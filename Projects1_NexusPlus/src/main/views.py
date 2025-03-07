from django.shortcuts import render

from category.models import Category


# Create your views here.

def main(request):
    categories = Category.objects.filter(is_main =True)
    ctx = {
        'categories': categories,
    }
    return render(request, 'index-2.html', ctx)