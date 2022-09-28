from django import forms
from .models import User

class LoginForm(forms.Form):
  username = forms.CharField(max_length=50, label='Nombre de Usuario')
  email = forms.EmailField(max_length=50, label='Email')
  password = forms.CharField(max_length=50, label='Contraseña', widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = [
        'username',
        'email',
        'password'
        ]

class SignupForm(forms.Form):
  username = forms.CharField(max_length=50, label='Nombre de Usuario')
  email = forms.EmailField(max_length=50, label='Email')
  password1 = forms.CharField(max_length=50, label='Contraseña', widget=forms.PasswordInput)
  password2 = forms.CharField(max_length=50, label='Confirmar Contraseña', widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = [
        'username',
        'email',
        'password1'
        'password2'
        ]