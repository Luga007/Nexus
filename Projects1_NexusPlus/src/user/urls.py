from . import views
from django.urls import path, include

urlpatterns = [
    path('login_view/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]