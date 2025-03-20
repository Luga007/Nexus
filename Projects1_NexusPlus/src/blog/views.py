from django.shortcuts import render
from category.models import Category
from django.db.models import Count
from . import models
from django.db.models import Prefetch
# Create your views here.
def blog(request):
    category = Category.objects.annotate(counts=Count('product'))
    blogs = models.Blog.objects.prefetch_related(
        Prefetch('images', queryset=models.BlogImage.objects.all(), to_attr='main_image'),
    )
    ctx = {
        'categories': category,
        'blogs': blogs,
    }
    return render(request, 'blog.html', ctx)

def post_list(request, pk):
    blogs = models.Blog.objects.get(pk=pk)
    blogs1 = (
        models.Blog.objects
        .prefetch_related(
            Prefetch('images', queryset=models.BlogImage.objects.all(), to_attr='main_image'),

        )
    )


    ctx = {
        'blogs': blogs,
        'blogs1': blogs1,
        'blogsId': 1,

    }
    return render(request, 'single-post.html', ctx)
