from django.http import JsonResponse
# from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import  permission_classes, authentication_classes ,api_view

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse({'data': serializer.data})
