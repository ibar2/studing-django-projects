from .serialization import snipetSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import snipet
# Create your views here.


# @api_view(['GET', 'POST', 'PUT'])
@csrf_exempt
def home(req):

    if req.method == 'GET':
        snip = snipet.objects.all()
        se = snipetSerializer(snip, many=True)
        return Response(se.data, content_type='application/xml')

    elif req.method == 'POST':
        data = JSONParser().parse(req)
        se = snipetSerializer(data=data)

        if se.is_valid():
            se.save()
            return Response(se.data, content_type='application/xml')
        return Response(se.error_messages)
    return Response('hello', content_type='application/xml')


@csrf_exempt
def all(req, pk):

    try:
        mo = snipet.objects.get(pk=pk)
    except snipet.DoesNotExist:
        return Response(status=404)

    if req.method == 'GET':
        se = snipetSerializer(mo)
        return Response(se.data)

    if req.method == 'PUT':
        data = JSONParser().parse(req)
        se = snipetSerializer(mo, data=data)
        if se.is_valid():
            se.save()
            return Response(se.data)
        return Response(se.error_messages)
