from django.urls import path
from api_cliente.views import *

urlpatterns = [
    path('eventos/', view = eventos),
    path('evento/<int:id>/', view = evento),
]