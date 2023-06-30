from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import secrets
from . import models
from .forms import SignUpForm
from urllib.parse import unquote
from django.http import HttpResponse


def homepage(req):
    return render(req, 'page/home.html')


def loginpage(req):
    if req.method == 'POST':
        user = get_object_or_404(models.User, username=req.POST['username'])
        if user is not None:
            return HttpResponse('user found')

        return HttpResponse('user not found')
    return render(req, 'page/Login.html')


def signup(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = unquote(req.POST['email'])
        password = req.POST['password']
        sing = SignUpForm(req.POST)
        if sing.is_valid():
            user = models.User.objects.create_user(username=username,
                                                   email=email,
                                                   password=password)
            user.save()
    return render(req, 'page/signup.html')


def generator(req):
    return render(req, 'page/generator.html')


def passwd(req):
    v = [secrets.choice("abcdefghijklmnopqrstuvwxyz-@#$&^!\
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ[]?_(*)|,;")
         for _ in range(12)]
    return JsonResponse({'password': "".join(v)})
