from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'cliente', views.ClienteViewSet)
router.register(r'mecanico', views.MecanicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index/', views.index, name= "index"),
]
