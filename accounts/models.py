from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    username = models.CharField(_('Username'), max_length=255)
    email = models.CharField(_('Email'), max_length=255, unique=True)
    city = models.CharField(_('City'), max_length=255, null=True, blank=True)
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'city']
