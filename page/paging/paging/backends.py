from page import models
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login
from django.shortcuts import render
import sys
sys.path.append('..')


class CustomModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Implement your custom authentication logic here
        # You can use the User model specified in AUTH_USER_MODEL setting for authentication
        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):
                print('verified')
                # login(request, user)
                return user
        except TypeError:
            return None

    def get_user(self, user_id):
        # Retrieve the User instance based on the user_id
        try:
            return self.objects.get(pk=user_id)
        except:
            return None