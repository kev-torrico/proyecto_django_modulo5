from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'cliente', views.ClienteViewSet)
router.register(r'mecanico', views.MecanicoViewSet)
router.register(r'coche', views.CocheViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index/', views.index, name= "index"),
    path('reparacion/', views.ReparacionCreateView.as_view(), name='reparacion-create-list')
]
