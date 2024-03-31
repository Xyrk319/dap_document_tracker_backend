from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from core.models.TimeStampedModel import TimeStampedModel
from core.models.SoftDeleteModel import SoftDeleteModel
from .role import Role
from django.db import models


class User(AbstractBaseUser, TimeStampedModel, SoftDeleteModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    remember_token = models.CharField(max_length=255, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'password',
        'role_id',
        ]
    objects = BaseUserManager()
    def __str__(self):
        return self.email
