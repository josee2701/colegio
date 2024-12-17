from rest_framework import serializers

from .models import Estudiante, Notas, Profesor


class EstudianteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Estudiante
        fields='__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Profesor
        fields='__all__'

class NotasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Notas
        fields='__all__'