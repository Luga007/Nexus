from django.shortcuts import render

def products(request):
    return render(request, 'product.html', {})
