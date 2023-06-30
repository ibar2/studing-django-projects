from .serialization import snipetSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import snipet
# Create your views here.


@csrf_exempt
def home(req):

    if req.method == 'GET':
        snip = snipet.objects.all()
        se = snipetSerializer(snip, many=True)
        return JsonResponse(se.data, safe=False)

    elif req.method == 'POST':
        data = JSONParser().parse(req)
        se = snipetSerializer(data=data)

        if se.is_valid():
            se.save()
            return JsonResponse(se.data, status=201)
        return JsonResponse(se.error_messages, status=400)


@csrf_exempt
def all(req, pk):

    try:
        mo = snipet.objects.get(pk=pk)
    except snipet.DoesNotExist:
        return HttpResponse(status=404)

    if req.method == 'GET':
        se = snipetSerializer(mo)
        return JsonResponse(se.data)

    if req.method == 'PUT':
        data = JSONParser().parse(req)
        se = snipetSerializer(mo, data=data)
        if se.is_valid():
            se.save()
            return JsonResponse(se.data)
        return JsonResponse(se.error_messages, status=400)
