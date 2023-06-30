from django import forms
from .models import customUser


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = customUser
        fields = ['username', 'full_name', 'address', 'password']
        labels = {
            'username': 'Username',
            'full_name': 'Full Name',
            'address': 'Address',
            'password': 'Password'
        }
