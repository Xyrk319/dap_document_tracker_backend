from django.contrib.auth.models import Permission
from django.db import models
from utils.TimeStampedModel import TimeStampedModel
from utils.SoftDeleteModel import SoftDeleteModel

class Role(TimeStampedModel, SoftDeleteModel):
    name = models.CharField(max_length=255, unique=True)
    permissions = models.ManyToManyField(Permission, related_name="role_permissions", blank=True)

    def __str__(self):
        return self.name
