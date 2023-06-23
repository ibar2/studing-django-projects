from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('login', views.loginpage, name='login'),
    path('signup', views.signup, name='signup'),
    path('generator', views.generator, name='generator')
]
