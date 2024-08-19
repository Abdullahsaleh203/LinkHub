from django.contrib.auth.forms import UserCreationForm

from .models import User

class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'password1', 'password2']
