from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView, status
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from category.models import Region
from .serializer import RegionSerializer

# 1.


class RegionApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        region = Region.objects.all()
        serializer = RegionSerializer(region, many=True)
        return Response({'results': serializer.data})

    def post(self, request):
        res = RegionSerializer(data=request.data)
        if res.is_valid():
            res.save()
            return Response({'success': res.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': res.errors}, status=status.HTTP_400_BAD_REQUEST)


class RegionApiViewPk(APIView):
    def get(self, request, pk):
        try:
            region = Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        res = RegionSerializer(region)
        return Response({'results': res.data})

    def put(self, request, pk):
        try:
            region = Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RegionSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': serializer.data})
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        region = Region.objects.get(pk=pk)
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 2.
class RegionGenericView(GenericAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def get(self, request):
        region = self.get_queryset()
        serializer = self.get_serializer(region, many=True)
        return Response({'results': serializer.data})

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class RegionGenericViewPk(GenericAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def get(self, request, *args, **kwargs):
        region = self.get_object()
        serializer = self.get_serializer(region)
        return Response({'results': serializer.data})

    def put(self, request, *args, **kwargs):
        region = self.get_object()
        serializer = self.get_serializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        region = self.get_object()
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#3
class RegionMixinsView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RegionMixinsViewPk(mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin,GenericAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



# 4.
class RegionGenericAPIView(ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class RegionDetailGenericAPIView(ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = 'slug'



# 5.
class RegionViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
