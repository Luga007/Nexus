from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from category.models import Region
from .serializer import RegionSerializer

class RegionViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer



class RegionGenericAPIView(ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [SearchFilter]
    lookup_field = ['title', 'description']


class RegionDetailGenericAPIView(ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = ['slug']
