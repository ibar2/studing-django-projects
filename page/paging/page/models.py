from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self) -> str:
        return self.username


class passwords(models.Model):
    owner = models.IntegerField()
    name = models.CharField(max_length=55)
    passwd = models.CharField(max_length=200, default=None)
    created_at = models.DateField(auto_now=True)
