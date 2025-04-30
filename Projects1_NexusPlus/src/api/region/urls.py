from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (RegionViewSet, RegionGenericAPIView, RegionDetailGenericAPIView, RegionApiView,
                    RegionApiViewPk, RegionGenericView, RegionGenericViewPk, RegionMixinsView, RegionMixinsViewPk)

router = DefaultRouter()
router.register(r'', RegionViewSet)

urlpatterns = [
    #1
    path('regionApi/', RegionApiView.as_view(), name='region-api'),
    path('regionApi/<int:pk>/', RegionApiViewPk.as_view(), name='region-api-pk'),
    #2
    path('regionGenericView/', RegionGenericView.as_view(), name='region-generic-view'),
    path('regionGenericView/<int:pk>/', RegionGenericViewPk.as_view(), name='region-generic-view'),
    #3
    path('regionMixinsView/', RegionMixinsView.as_view(), name='region-mixins-view'),
    path('regionMixinsView/<int:pk>/', RegionMixinsViewPk.as_view(), name='region-mixins-view'),
    #4
    path('regionv/', RegionGenericAPIView.as_view(), name='region'),
    path('regionv/<slug:slug>/', RegionDetailGenericAPIView.as_view(), name='region_detail'),
    # 5
    path('simple/', include(router.urls)),
]