from django.urls import path, include


urlpatterns = [
    path('category/', include('api.category.urls')),
    path('blog/', include('api.blog.urls')),
    path('user/', include('api.user.urls')),
    path('product/', include('api.product.urls')),
    path('region/', include('api.region.urls')),
    path('blog/', include('api.blog.urls')),
]