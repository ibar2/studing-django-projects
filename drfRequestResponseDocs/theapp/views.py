from .serialization import usersSerializer
from .models import snipet
from rest_framework import generics


class all(generics.ListCreateAPIView):
    queryset = snipet.objects.all()
    serializer_class = usersSerializer


class detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = snipet.objects.all()
    serializer_class = usersSerializer
