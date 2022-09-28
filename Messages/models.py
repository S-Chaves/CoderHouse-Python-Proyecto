from email.policy import default
from django.db import models
from Login.models import User
from datetime import datetime

# Create your models here.
class Message(models.Model):
  emisor = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='emisor')
  receptor = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='receptor')
  date = models.DateTimeField(null=False, blank=False, default=datetime.now,)
  body = models.TextField(null=False, blank=False)
  leido = models.BooleanField(null=False, blank=False, default=False)
