from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import status

from product.models import Product
from .serializers import ProductSerializer



@api_view(['GET', 'POST'])
def aquire_ctg_list(request):
    if request.method == 'GET':
        product = Product.objects.all()
        result = ProductSerializer(product, many=True)
        return Response({'result':result.data})
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': 'success'}, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def fraction_ctg(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        result = ProductSerializer(product)
        return Response({'result':result.data})
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': 'success'}, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






