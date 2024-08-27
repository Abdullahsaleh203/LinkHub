from django.db.models import Q
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
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    users = User.objects.filter(name__icontains=query)
    users_serializer = UserSerializer(users, many=True)

    posts = Post.objects.filter(
        Q(body__icontains=query, is_private=False) | 
        Q(created_by_id__in=list(user_ids), body__icontains=query)
    )

    posts_serializer = PostSerializer(posts, many=True)

    return JsonResponse({
        'users': users_serializer.data,
        'posts': posts_serializer.data
    }, safe=False)
