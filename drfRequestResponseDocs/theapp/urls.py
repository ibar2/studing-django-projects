from django.urls import path
from . import views


urlpatterns = [
    path('snipet/', views.home, name='snipet')
]
