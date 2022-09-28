from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Avatar(models.Model):
  image = models.ImageField(upload_to='avatars', null=True, blank=True)

class User(AbstractUser):
  USERNAME_FIELD = 'username'

  username = models.CharField(unique=True, max_length=50)
  email = models.EmailField(unique=True, null=False)
  name = models.CharField(max_length=50)
  description = models.TextField()
  web_page = models.CharField(max_length=50)
  avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, null=True, blank=True)
