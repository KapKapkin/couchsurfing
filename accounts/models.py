from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

import uuid

class CustomUser(AbstractUser):
    id = models.UUIDField(
        _('id'), 
        primary_key=True, 
        default=uuid.uuid4,
        editable=False,
    )
    username = models.CharField(_('username'), max_length=150)
    email = models.CharField(_('Email'), max_length=255, unique=True)
    city = models.CharField(_('City'), max_length=255, null=True, blank=True)
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])

    def __str__(self):
        return self.username
    
