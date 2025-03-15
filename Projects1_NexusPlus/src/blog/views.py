from django.shortcuts import render
from category.models import Category
from django.db.models import Count
# Create your views here.
def blog(request):
    category = Category.objects.annotate(counts=Count('product'))
    ctx = {
        'categories': category,
    }
    return render(request, 'blog.html', ctx)
