from django.contrib.auth.models import AbstractBaseUser
from utils.TimeStampedModel import TimeStampedModel
from utils.SoftDeleteModel import SoftDeleteModel
from .role import Role
from django.db import models


class User(AbstractBaseUser, TimeStampedModel, SoftDeleteModel):
    email = models.EmailField(max_length=255, unique=True)
    remember_token = models.CharField(max_length=255, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
