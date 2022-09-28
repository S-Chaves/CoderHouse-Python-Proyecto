from django import forms
from .models import User

class MessageForm(forms.Form):
  body = forms.CharField(widget=forms.Textarea)

  class Meta:
    fields = ['body']