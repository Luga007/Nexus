from django.shortcuts import render
from category.models import Category
from django.db.models import Count
from . import models
from django.db.models import Prefetch
from .models import Blog
from django.core.paginator import Paginator
from .forms import EmailForm
from django.core.mail import send_mail
from product.models import Product, ProductImage


def blog(request):
    page = request.GET.get('page', 1)
    category = Category.objects.annotate(counts=Count('product'))
    blogs = models.Blog.objects.prefetch_related(
        Prefetch('images', queryset=models.BlogImage.objects.all(), to_attr='main_image'),
    )
    category_blog = Blog.objects.annotate(counts=Count('id'))
    paginator = Paginator(blogs, 2)
    page_obj = paginator.get_page(page)


    ctx = {
        'categories': category,
        'blogs': blogs,
        'category_blog': category_blog,
        'page_obj': page_obj,
        'countOfBlogs': page,
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

    success = False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['to_email']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']

            send_mail(name, message, '', [to_email])
            success = True
    else:
        form = EmailForm()

    ctx = {
        'blogs': blogs,
        'blogs1': blogs1,
        'blogsId': pk,
        'category_blog': category_blog,
        'form': form
    }
    return render(request, 'single-post.html', ctx)
