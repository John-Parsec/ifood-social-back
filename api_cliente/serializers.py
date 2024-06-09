from rest_framework import serializers
from .models import *

def get_model_serializer(model_):
    class ModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_
            fields = '__all__'
    return ModelSerializer

def EventoSerializer():
    class EventoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Evento
            fields = '__all__'
    return EventoSerializer