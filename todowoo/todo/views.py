from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.contrib.auth import login
# Create your views here.


def signup(req):
    if req.method == 'POST':
        if req.POST['password1'] == req.POST['password1']:
            user = User(username=req.POST['username'], password=req.POST['password1'])
            user.save()
            login(req, user)
            return redirect('success')
        else:
            HttpResponseNotFound('404')
    return render(req, "todo/signup.html", {'form': UserCreationForm})


def success(req):
    return render(req, 'todo/success.html')
