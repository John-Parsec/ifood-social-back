from django.urls import path
from api_cliente.views import *

urlpatterns = [
    path('eventos/', eventos),
    path('evento/<int:id>/', evento),
]