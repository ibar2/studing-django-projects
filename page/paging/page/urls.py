from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('generator/', views.generator, name='generator'),
    path('generate/', views.passwd, name='generate'),
    path('strength-checker/', views.strengthchecker, name='checker'),
    path('checking/', views.cheking, name='checking'),
    path('dash/', views.dashboard, name='dashboard'),
    path('addpass/', views.addpass, name='addpass')
]
