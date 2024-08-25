from django.http import JsonResponse

from account.serializers import UserSerializer
from account.models import User

from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import  permission_classes, authentication_classes ,api_view
from .form import PostForm

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def post_list_profile(request, id):
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(created_by_id=id)

    posts_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)

    return JsonResponse({
        'user':user_serializer.data,
        'posts':posts_serializer.data},safe=False)

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

