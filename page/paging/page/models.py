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
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=55)
    objects = UserManager()

    USERNAME_FIELD = 'username'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    @property
    def is_admin(self):
        return True

    def __str__(self) -> str:
        return self.username


class dat(models.Model):
    data = models.TextField()
    comment = models.CharField(max_length=55, null=True, blank=True)

    def __str__(self) -> str:
        return self.data


class meaw(models.Model):
    cl = models.CharField(max_length=44, blank=True, null=True)
