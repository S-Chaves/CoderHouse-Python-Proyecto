from django import forms
from Login.models import User

class EditProfileForm(forms.Form):
  name = forms.CharField(max_length=30, required=False, label='Nombre')
  email = forms.EmailField(required=True)
  web_page = forms.CharField(max_length=50, required=False, label='Página Web')
  description = forms.CharField(max_length=50, widget=forms.Textarea, required=False, label='Decripción')
  avatar = forms.ImageField(required=False)

  class Meta:
    model = User
    fields = ['name', 'email', 'web_page', 'description', 'avatar']