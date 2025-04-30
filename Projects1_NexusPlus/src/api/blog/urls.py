from django.urls import path, include
from .views import (obtain_list_tg, fraction_ctg, BlogViewSet, BlogViewPk, BlogMixinsView,
                    BlogGenericView, BlogGenericViewPk, BlogMixinsViewPk, BlogViewSets)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BlogViewSets, basename='blog')
urlpatterns = [
    path('', obtain_list_tg, name='obtain_list_tg'),
    path('<int:pk>/', fraction_ctg, name='fraction_ctg'),
    path('blogT/', BlogViewSet.as_view(), name='blogT'),
    path('blogT/<int:pk>/', BlogViewPk.as_view(), name='blogPk'),

    path('blogmix/', BlogMixinsView.as_view(), name='Blogmix'),
    path('blogmixPk/<int:pk>/', BlogMixinsViewPk.as_view(), name='BlogmixPk'),

    path('blogPk/', BlogGenericView.as_view(), name='blog_generic'),
    path('blogPk/<int:pk>/', BlogGenericViewPk.as_view(), name='blog_genericPk'),

    path('simple/', include(router.urls)),


]