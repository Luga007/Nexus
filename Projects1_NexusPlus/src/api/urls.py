from django.urls import path, include


urlpatterns = [
    path('category/', include('api.category.urls')),
    path('blog/', include('api.blog.urls')),
    path('user/', include('api.user.urls')),
]