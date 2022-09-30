from django import forms
from .models import Blog
from ckeditor.widgets import CKEditorWidget

class CreateBlogForm(forms.Form):
  title = forms.CharField(max_length=50, label='Título del Blog')
  subtitle = forms.CharField(max_length=50, label='Subtitulo del Blog')
  image = forms.ImageField(label='Imágen')
  body = forms.CharField(label='Cuerpo del Blog', widget = CKEditorWidget())

  class Meta:
    model = Blog
    fields = ['title', 'subtitle', 'body', 'image']

class EditBlogForm(forms.Form):
  title = forms.CharField(max_length=50, label='Título del Blog')
  subtitle = forms.CharField(max_length=50, label='Subtitulo del Blog')
  body = forms.CharField(label='Cuerpo del Blog', widget = CKEditorWidget())
  image = forms.ImageField(label='Imágen', required=False)

  class Meta:
    model = Blog
    fields = ['title', 'subtitle', 'body', 'image']