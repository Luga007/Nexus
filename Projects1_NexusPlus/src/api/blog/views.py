from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import status, APIView
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet


from .serializers import BlogSerializer
from blog.models import Blog

# 0. ------------------------------------------------------------------------------------------

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

# 1. ---------------------------------------------------------------------------------------------------

class BlogViewSet(APIView):
    def get(self, request):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return Response({'results': serializer.data})

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogViewPk(APIView):
    def get(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        res = BlogSerializer(blog)
        return Response({'results': res.data})

    def put(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'results': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 2. --------------------------------------------------------

class BlogGenericView(GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request):
        blog = self.get_queryset()
        serializer = self.get_serializer(blog, many=True)
        return Response({'results': serializer.data})


    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class BlogGenericViewPk(GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def get(self, request, *args, **kwargs):
        blog = self.get_object()
        serializer = self.get_serializer(blog)
        return Response({'results': serializer.data})

    def put(self, request, *args, **kwargs):
        blog = self.get_object()
        serializer = self.get_serializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        blog = self.get_object()
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# 4. -------------------------------------------------------



class BlogMixinsView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BlogMixinsViewPk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BlogViewSets(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer















