from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=50,widget=forms.EmailInput,  required=True)
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']
        
class ChangeUser(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']
        