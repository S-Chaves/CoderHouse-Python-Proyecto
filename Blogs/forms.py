from django import forms
from .models import Blog

class CreateBlogForm(forms.Form):
  title = forms.CharField(max_length=50, label='Título del Blog')
  subtitle = forms.CharField(max_length=50, label='Subtitulo del Blog')
  # body = forms.Textarea()
  image = forms.ImageField(label='Imágen')

  class Meta:
    model = Blog
    fields = [
        'title',
        'subtitle',
        'image'
        ]