from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET', 'POST'])
def eventos(request):
    if request.method == 'GET':
        evento = Evento.objects.all()
        serializer = get_model_serializer(evento, many=True)
        return Response(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = get_model_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, safe=False)
        return Response(serializer.errors, safe=False)

@api_view(['GET', 'DELETE', 'PUT'])
def evento(request, id):
    if request.method == 'DELETE':
        evento = Evento.objects.get(id=id)
        evento.delete()
        return Response({'message': 'Evento deletado com sucesso!'}, safe=False)
    elif request.method == 'PUT':
        evento = Evento.objects.get(id=id)
        serializer = get_model_serializer(evento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, safe=False)
        return Response(serializer.errors, safe=False)
    elif request.method == 'GET':
        evento = Evento.objects.get(id=id)
        serializer = get_model_serializer(evento)
        return Response(serializer.data, safe=False)