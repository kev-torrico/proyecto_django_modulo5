from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'cliente', views.ClienteViewSet)
router.register(r'mecanico', views.MecanicoViewSet)
router.register(r'coche', views.CocheViewSet)

urlpatterns = [
    path('index/', views.index, name= "index"),
    path('reparacion/', views.ReparacionCreateView.as_view(), name='reparacion-create-list'),
    path('coche/filtrar/nuevo', views.coches_nuevos, name='coches-nuevos'),
    path('coche/filtrar/usado', views.coches_usados, name='coches-usados'),
    path('', include(router.urls)),
]
