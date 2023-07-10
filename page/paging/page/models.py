from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        user = self.model(username=username,
                          email=email,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self):
        raise NotImplementedError


class User(AbstractBaseUser):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=55)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = 'username'

    def __str__(self) -> str:
        return self.username


class dat(models.Model):
    data = models.TextField()
    comment = models.CharField(max_length=55, null=True, blank=True)

    def __str__(self) -> str:
        return self.data


class meaw(models.Model):
    cl = models.CharField(max_length=44, blank=True, null=True)
