from django.urls import path
from .views import (aquire_ctg_list, fraction_ctg, ProductGeneric,
                    ProductGenericPk, ProductMixins, ProductMixinsPk,
                    ProductAPIView, ProductAPIViewPk, ProductListAPIView, ProductListAPIViewPk)

urlpatterns = [
    path('productApi/', aquire_ctg_list, name='aquire_ctg_list'),
    path('product<int:pk>/', fraction_ctg, name='fraction_ctg'),

    #1
    path('productapview/', ProductAPIView.as_view(), name='ProductAPIView'),
    path('productapview/<int:pk>/', ProductAPIViewPk.as_view(), name='ProductAPIViewPk'),

    #2
    path('productgeneric/', ProductGeneric.as_view(), name='ProductGeneric'),
    path('productgeneric/<int:pk>/', ProductGenericPk.as_view(), name='ProductGenericPk'),

    #3
    path('productmixins/', ProductMixins.as_view(), name='ProductMixins'),
    path('productmixins/<int:pk>/', ProductMixinsPk.as_view(), name='ProductMixinsPk'),

    #4
    path('productlistapiview/', ProductListAPIView.as_view(), name='ProductListAPIView'),
    path('productlistapiview/<int:pk>/', ProductListAPIViewPk.as_view(), name='ProductListAPIViewPk'),

]