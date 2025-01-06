from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from userauth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['username','email','password1','password2']
        
class LoginForm(AuthenticationForm):
    class Meta:
        model= User
        fields= ['email','password']