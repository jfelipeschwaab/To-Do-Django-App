from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
          
    class Meta: ##Utilizado para clareza(Saber qual modelo se está usando) e usado para facilitar a manutenção 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    