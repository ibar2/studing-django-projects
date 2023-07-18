from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from . import models, forms
# Register your models here.
admin.site.unregister(Group)


class Custom(UserAdmin):
    add_form = forms.SignUpForm
    form = forms.SignUpForm
    model = models.User
    list_display = ['username', 'is_active']


admin.site.register(models.User, Custom)

