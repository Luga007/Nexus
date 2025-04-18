from rest_framework.response import Response
from rest_framework.views import status
from category.models import Category
from .serializers import CategorySerializer
from rest_framework.decorators import api_view



@api_view(['GET', 'POST'])
def get_list_ctg(request):
    if request.method == 'GET':
        category = Category.objects.all()
        result = CategorySerializer(category, many=True)
        print(result.data)
        return Response({'result': result.data})
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            results = serializer.save()
            return Response({"data": "success"}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_ctg(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Could not find category'})

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

