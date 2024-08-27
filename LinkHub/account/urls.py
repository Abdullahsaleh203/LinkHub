from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api


urlpatterns = [
    path('me/', api.me, name='me'),
    path('signup/', api.signup, name='signup'),
<<<<<<< HEAD
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
    path('friends/<uuid:pk>/', api.friends, name='friends'),
    path('friends/<uuid:pk>/request/', api.send_friendship_request, name='send_friendship_request'),
    path('friends/<uuid:pk>/<str:status>/', api.handle_request, name='handle_request'),
=======
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('friends/<uuid>:pk>', api.friends, name='friends'),
    path('friends/<uuid>:pk>/request/', api.send_friendship_request, name='send_friendship_request'),
    path('friends/<uuid>:pk>/<str:status>/', api.handle_request, name='handler_request'),
>>>>>>> f6c3c75835d146bee922e10b0ce063a39c94a2d6
]
