from django.http import JsonResponse
from django.shortcuts import render


def check_password_strength(request):
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
