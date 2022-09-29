from django import forms
from Login.models import User

class EditProfileForm(forms.Form):
  name = forms.CharField(max_length=30, required=False)
  email = forms.EmailField(required=True)
  web_page = forms.CharField(max_length=50, required=False)
  description = forms.CharField(max_length=50, widget=forms.Textarea, required=False)
  avatar = forms.ImageField(required=False)

  class Meta:
    model = User
    fields = ['name', 'email', 'web_page', 'description', 'avatar']