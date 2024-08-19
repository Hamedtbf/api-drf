from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework import status


# Create your views here.


class PostList(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PostDetail(APIView):

    def get(self, request, item):
        post = Post.objects.get(pk=item)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, item):
        post = Post.objects.get(pk=item)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, item):
        post = Post.objects.get(pk=item)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
