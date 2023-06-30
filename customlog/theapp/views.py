from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from .models import customUser


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = get_object_or_404(customUser, username=username)
        if user is not None:
            verify = user.check_password(password)
            if not verify:
                raise Exception('password not matched')
            login(request, user)
            return render(request, 'home.html')
        else:
            message = "Invalid username/password"
            return render(request, 'login.html', {'message': message})
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            full_name = form.cleaned_data.get('full_name')
            address = form.cleaned_data.get('address')
            password = form.cleaned_data.get('password')
            user = customUser.objects.create_user(username=username, full_name=full_name,
                                                  password=password, address=address)
            user.save()
            login(request, user)
            return render(request, 'home.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
