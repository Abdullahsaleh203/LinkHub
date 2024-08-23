from django.http import JsonResponse
# from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import  permission_classes, authentication_classes ,api_view
from .form import PostForm
@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def post_create(request):
    form = PostForm(request.data)
    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data ,safe=False)
    else:
        return JsonResponse({'error':'Add somethting here'})

