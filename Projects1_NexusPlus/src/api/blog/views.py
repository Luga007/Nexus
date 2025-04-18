from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import status

from .serializers import BlogSerializer
from blog.models import Blog


@api_view(['GET', 'POST'])
def obtain_list_tg(request):
    if request.method == 'GET':
        blog = Blog.objects.all()
        result = BlogSerializer(blog, many=True)
        return Response({'results': result.data})
    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return Response({'data': 'success'}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def fraction_ctg(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        result = BlogSerializer(blog)
        return Response({'results': result.data})

    elif request.method == 'PUT':
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

