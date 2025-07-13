from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from .serializers import ClienteSerializer, MecanicoSerializer, CocheSerializer, ReparacionSerializer
from .models import Cliente, Mecanico, Coche, Reparacion
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

class ReparacionCreateView (generics.CreateAPIView, generics.ListAPIView):
    queryset= Reparacion.objects.all()
    serializer_class= ReparacionSerializer

@api_view(['GET'])
def coches_nuevos(request):
    try:
        coches = Coche.objects.filter(tipo="nuevo")
        return JsonResponse(
            CocheSerializer(coches, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)

@api_view(['GET'])
def coches_usados(request):
    try:
        coches = Coche.objects.filter(tipo="usado")
        return JsonResponse(
            CocheSerializer(coches, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)