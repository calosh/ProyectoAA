from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class LoginForm(forms.Form):

    username = forms.CharField(max_length=50,)
    password = forms.CharField(max_length=50,
        widget = forms.TextInput(attrs = {
            'type':'password'
            }))



class UserForm(UserCreationForm):
    email = forms.EmailField()

    
    class Meta:
        model = User
        fields = ("username",)

    