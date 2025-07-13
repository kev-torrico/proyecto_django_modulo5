from rest_framework import serializers
from .models import Cliente, Mecanico

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class MecanicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mecanico
        fields = '__all__'