from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import status, APIView

from product.models import Product
from .serializers import UserSerializer
from user.models import Profile
from ..product.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def receive_ctg_list(request):
    if request.method == 'GET':
        profile = Profile.objects.all()
        results = UserSerializer(profile, many=True)
        return Response({'result': results.data})
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": "success"}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def grain_ctg(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response({'error': 'Profile does not exist'})

    if request.method == 'GET':
        serializer = UserSerializer(profile)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductViewSet(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'result': serializer.data})
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def somethingTOtest(request):
    pass


