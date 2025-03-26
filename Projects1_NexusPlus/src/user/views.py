from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get['username']
            password = request.POST.get['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('main')
    form = LoginForm()
    ctx = {
        'form': form
    }
    return render(request, 'login.html', ctx)

def register(request):
    ctx = {

    }
    return render(request, 'register.html', ctx)

def logout_view(request):
    logout(request)
    return ('main')