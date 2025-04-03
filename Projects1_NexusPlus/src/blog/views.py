from django.shortcuts import render
from category.models import Category
from django.db.models import Count
from . import models
from django.db.models import Prefetch
from .models import Blog
# Create your views here.
def blog(request):
    category = Category.objects.annotate(counts=Count('product'))
    blogs = models.Blog.objects.prefetch_related(
        Prefetch('images', queryset=models.BlogImage.objects.all(), to_attr='main_image'),
    )
    category_blog = Blog.objects.annotate(counts=Count('id'))
    ctx = {
        'categories': category,
        'blogs': blogs,
        'category_blog': category_blog,
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
    category_blog = Blog.objects.annotate(counts=Count('id'))


    ctx = {
        'blogs': blogs,
        'blogs1': blogs1,
        'blogsId': pk,
        'category_blog': category_blog
    }
    return render(request, 'single-post.html', ctx)
