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
        db_index=True,
    )

    username = models.CharField(_('username'), max_length=150)
    email = models.CharField(_('Email'), max_length=255, unique=True)
    city = models.CharField(_('City'), max_length=255, null=True, blank=True)
    avatar = models.FileField(upload_to='avatars/', blank=True)
    room_image = models.FileField(upload_to='rooms/', blank=True)
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_index')
        ]

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

    def __str__(self):
        return self.username
    
