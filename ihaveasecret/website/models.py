from django.db import models

class Message(models.Model):
  message = models.TextField()
  email = models.EmailField(blank=True)
  date = models.DateTimeField(auto_now_add=True)
  location = models.CharField(max_length=200, blank=True)
  public = models.BooleanField(default=True)
