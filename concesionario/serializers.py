from rest_framework import serializers
from .models import Cliente, Mecanico, Coche, Reparacion

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class MecanicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mecanico
        fields = '__all__'
class CocheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coche
        fields = '__all__'
class ReparacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reparacion
        fields = '__all__'