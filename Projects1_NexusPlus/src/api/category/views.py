from urllib import request

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from category.models import Category
from .serializers import CategorySerializer




@api_view(['GET', 'POST'])
def get_list_ctg(request):
    if request.method == 'GET':
        category = Category.objects.all()
        result = CategorySerializer(category, many=True)
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


class CategoryViewSet(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response({'result': serializer.data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailPk(APIView):
    def get(self, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error': 'Could not find category'})
        res = CategorySerializer(category)
        return Response({'result': res.data})

    def put(self, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error': 'Could not find category'})
        res = CategorySerializer(category, data=request.data)
        if res.is_valid():
            res.save()
            return Response({'result': res.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': res.errors}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        category = Category.obejcts.get(pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

