from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets
from .serial import UserSerializer, GroupSerializer
# Create your views here.


class userview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class groupview(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
