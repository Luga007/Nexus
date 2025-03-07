from django.shortcuts import render
from category.models import Category
from Projects1_NexusPlus.src.category.models import Category


# Create your views here.

def main(request):
    categories = Category.objects.all(is_main=True)
    ctx = {
        'categories': categories,
    }
    return render(request, 'index-2.html', ctx)