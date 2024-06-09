from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *

# Create your views here.
def eventos(request):
    evento = Evento.objects.all()
    serializer = get_model_serializer(evento, many=True)
    return JsonResponse(serializer.data, safe=False)

def evento(request, id):
    evento = Evento.objects.get(id=id)
    serializer = get_model_serializer(evento)
    return JsonResponse(serializer.data, safe=False)