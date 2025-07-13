from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ClienteSerializer, MecanicoSerializer, CocheSerializer
from .models import Cliente, Mecanico, Coche
# Create your views here.


def index(request):
    return HttpResponse("Este proyecto lo creo Kevin Villca Torrico")

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class MecanicoViewSet(viewsets.ModelViewSet):
    queryset = Mecanico.objects.all()
    serializer_class = MecanicoSerializer

class CocheViewSet(viewsets.ModelViewSet):
    queryset = Coche.objects.all()
    serializer_class = CocheSerializer