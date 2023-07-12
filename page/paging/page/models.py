from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self) -> str:
        return self.username


class dat(models.Model):
    data = models.TextField()
    comment = models.CharField(max_length=55, null=True, blank=True)

    def __str__(self) -> str:
        return self.data


class meaw(models.Model):
    cl = models.CharField(max_length=44, blank=True, null=True)
