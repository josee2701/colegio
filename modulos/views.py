from django.shortcuts import render
from rest_framework import viewsets

from .models import Estudiante, Notas, Profesor
from .serializers import (EstudianteSerializer, NotasSerializer,
                          ProfesorSerializer)

# Create your views here.


class EstudianteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD de Sending_Commands.
    """
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    
class ProfesorViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD de Sending_Commands.
    """
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    
class NotasViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD de Sending_Commands.
    """
    queryset = Notas.objects.all()
    serializer_class = NotasSerializer

