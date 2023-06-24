from django.urls import path
from . import views


urlpatterns = [
    path('snipet', views.all.as_view(), name='snipet'),
    path('snipet/<int:pk>', views.detail.as_view(), name='detail'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
