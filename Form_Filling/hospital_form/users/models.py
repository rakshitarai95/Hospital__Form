from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


# class Role(models.Model):
#     name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name


class User(AbstractUser):
    CHOICES = (
        ('Client', 'Client'),
    )
    username = None
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(max_length=10, choices=CHOICES, default='Client')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
