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
        print(models.User.objects.all())
        print()
        print(models.dat.objects.all())
        # user = get_object_or_404(models.User, username=req.POST['username'])
        user = get_object_or_404(models.dat, data=req.POST['username'])
        if user is not None:
            return HttpResponse('user found')

        return HttpResponse('user not found')
    return render(req, 'page/Login.html')


def signup(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = unquote(req.POST['email'])
        password = req.POST['password']
        # sing = SignUpForm(req.POST)
        # if sing.is_valid():
        #     user = models.User.objects.create_user(username=username,
        #                                            email=email,
        #                                            password=password)
        mod = models.dat()
        mod.data = str(password)
        mod.save()

    return render(req, 'page/signup.html')


def generator(req):
    return render(req, 'page/generator.html')


def passwd(req):
    v = [secrets.choice("abcdefghijklmnopqrstuvwxyz-@#$&^!\
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ[]?_(*)|,;")
         for _ in range(12)]
    return JsonResponse({'password': "".join(v)})


def strengthchecker(req):
    return render(req, 'page/checker.html')


def cheking(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        password = request.POST.get('password', None)

        # Check password strength criteria
        length_ok = len(password) >= 8
        uppercase_ok = any(c.isupper() for c in password)
        lowercase_ok = any(c.islower() for c in password)
        digits_ok = any(c.isdigit() for c in password)
        symbols_ok = any(
            c in '!@#$%^&*()_+-=[]{}|\\;\':",./<>?' for c in password)

        if length_ok and uppercase_ok and lowercase_ok and digits_ok and symbols_ok:
            response_data = {'result': 'strong'}
        else:
            response_data = {'result': 'weak'}

        return JsonResponse(response_data)

    return render(request, 'password_check.html')
