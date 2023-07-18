from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, Http404
import secrets
from django.contrib.auth import authenticate, login, logout
from . import models
from .forms import SignUpForm
from urllib.parse import unquote
import requests as re
from hashlib import sha1

def homepage(req):
    return render(req, 'page/home.html')


def logoutUser(request):
    """
    Log the user out of the application.
    """
    logout(request)
    return redirect('/')


def loginpage(req):
    if req.method == 'POST':
        user = authenticate(
            username=req.POST['username'], password=req.POST['password'])
        if user is not None:
            login(req, user)
            return redirect('/dash')
        else:
            raise Http404('user not found')

    return render(req, 'page/Login.html')


def signup(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = unquote(req.POST['email'])
        password = req.POST['password']
        if password == req.POST['password2']:
            sing = SignUpForm(req.POST)
            if sing.is_valid():
                user = models.User.objects.create_user(username=username,
                                                       email=email,
                                                       password=password)
                user.save()

                login(req, user)

                return redirect('/')
        else:
            raise render(req, 'page/signup.html')

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
        hsh = sha1(password.encode())
        res = re.get(f'https://api.pwnedpasswords.com/range/{hsh.hexdigest()[:5]}')
        if res.status_code == 200:
            pwned = 'This password is Leaked'
        else:
            pwned = 'This is strong password'

        # Check password strength criteria
        length_ok = len(password) >= 8
        uppercase_ok = any(c.isupper() for c in password)
        lowercase_ok = any(c.islower() for c in password)
        digits_ok = any(c.isdigit() for c in password)
        symbols_ok = any(
            c in '!@#$%^&*()_+-=[]{}|\\;\':",./<>?' for c in password)

        if length_ok and uppercase_ok and lowercase_ok and digits_ok and symbols_ok:
            response_data = {'result': pwned}
        else:
            response_data = {'result': 'This is a weak password weak'}

        return JsonResponse(response_data)

    return render(request, 'password_check.html')


def dashboard(req):
    if req.user.is_authenticated:
        mod = models.passwords.objects.filter(
            owner=req.user.pk)
        print(mod)
        return render(req, 'page/dash.html', {'pass': mod})
    
    return redirect('/login')


def addpass(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            name = req.POST['name']
            passwd = req.POST['pass']
            mod = models.passwords.objects.create(
                owner=req.user.pk, name=name, passwd=passwd)
            mod.save()
        g = models.passwords.objects.filter(owner=req.user.pk)
        return render(req, 'page/addpass.html', {'pass' :g })
    else:
        return redirect('/login')
