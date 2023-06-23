from django.shortcuts import render
from .serialization import usersSerializer
from .models import snipet
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@api_view(['GET', 'POST', 'PUT'])
@csrf_exempt
def home(req, format=None):

    if req.method == 'GET':
        snip = snipet.objects.all()
        se = usersSerializer(snip, many=True)
        return Response(se.data)

    elif req.method == 'POST':
        data = JSONParser().parse(req)
        se = usersSerializer(data=data)

        if se.is_valid():
            se.save()
            return Response(se._data)
        return Response(se.error_messages)
