from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class customManager(BaseUserManager):
    def create_user(self, username, full_name, password, address=None):
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            username=username,
            full_name=full_name,
            address=address,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, full_name, password, address=None):
        user = self.create_user(
            username=username,
            password=password,
            full_name=full_name,
            address=address,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class customUser(AbstractBaseUser):
    username = models.CharField(max_length=55, unique=True)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=130, null=True, blank=True)

    objects = customManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
