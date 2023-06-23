from django.shortcuts import render


def homepage(req):
    return render(req, 'page/home.html')


def loginpage(req):
    return render(req, 'page/Login.html')


def signup(req):
    return render(req, 'page/signup.html')


def generator(req):
    return render(req, 'page/generator.html')
