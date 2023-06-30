from django.urls import path
from .views import check_password_strength


urlpatterns = [
    path('check_password_strength/', check_password_strength,
         name='check_password_strength'),
]
