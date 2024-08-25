from django.http import JsonResponse
from rest_framework.decorators import  permission_classes, authentication_classes ,api_view

from post.serializers import PostSerializer
from post.models import Post
from account.models import User
from account.serializers import UserSerializer


@api_view(['POST'])
def search(request):
    data = request.data
    query = data['query']
    users = User.objects.filter(name__icontains=query)
    users_serializer = UserSerializer(users, many=True)
    post= Post.objects.filter(title__icontains=query)
    post_serializer = PostSerializer(post, many=True)
    return JsonResponse({'users': users_serializer.data, 'posts': post_serializer.data}, safe=False)
    # return JsonResponse(users_serializer.data, safe=False)
  
