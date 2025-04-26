from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegionViewSet, RegionGenericAPIView, RegionDetailGenericAPIView

router = DefaultRouter()
router.register(r'', RegionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('region/', RegionGenericAPIView.as_view(), name='region' ),
    path('region/<int:pk>/', RegionDetailGenericAPIView.as_view(), name='region_detail')
]