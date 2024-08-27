from django.http import JsonResponse
from rest_framework.decorators import  permission_classes, authentication_classes ,api_view 
from .forms import SignupForm

from .models import  User, FriendshipRequest
from .serializers import UserSerializer , FriendshipRequestSerializer

@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id':request.user.id,
        'name':request.user.name,
        'email':request.user.email,
        'avatar': request.user.get_avatar()

    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = "Hello,! Your account has been created."

    form = SignupForm({
        'email':data.get('email'),
        'name':data.get('name'),
        'password1':data.get('password1'),
        'password2':data.get('password2'),
        })
    if form.is_valid():
        user = form.save()
        user.is_active = False
        user.save()

        # Send verification email later
    else:
        message = "Error: Account could not be created."
        
    return JsonResponse({'message': message})

@api_view(['GET'])
def friends(request,pk):
    user = User.object.get(pk=pk)
    request = []
    if user == request.user:
        requests = FriendshipRequest.objects.filter(created_for=request.user)
        request = FriendshipRequest(requests,many=True)
        request =request.data
        
    friends = user.friends.all()
    
    return JsonResponse({'user':UserSerializer(user).data,
                        'friends':UserSerializer(friends , many=True).data,
                        'requests':request
                        },safe=False)
@api_view(['POST'])
def send_friendship_request(request,pk):
    user = User.object.get(pk=pk)
    friendship_request = FriendshipRequest.objects.create(created_for=user,created_by=request.user)
    
    return JsonResponse({'message':'friendship request created'})


@api_view(['POST'])
def handle_request(request,pk,status):
    user = User.objects.get(pk=pk)
    friendship_request = FriendshipRequest.objects.filter(created_for=request.user).get(created_by=user)
    friendship_request.status = status
    friendship_request.save()

    user.friends.add(request.user)
    user.friends_count = user.friends_count + 1
    user.save()
    
    request_user = request.user
    request_user.friends_count = request_user.friends_count + 1
    request_user.save()
    
    return JsonResponse({'message': 'Friendship request updated'})
