from django.db import models
from Login.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
  title = models.CharField(null=False, blank=False, max_length=50)
  subtitle = models.CharField(max_length=50)
  body = RichTextField(blank=False,null=False)
  author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  date = models.DateField(null=False, blank=False)
  image = models.ImageField(upload_to='blogs')