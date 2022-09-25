from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToOneRel(CustomUser, on_delete=models.CASCADE)
