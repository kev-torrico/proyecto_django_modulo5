from django.contrib import admin
from .models import Cliente, Mecanico, Coche, Reparacion
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display=('ci', 'nombre', 'apellidos', 'direccion', 'telefono')
    ordering = ('nombre',)
    search_fields = ('nombre',)

admin.site.register(Cliente, ClientAdmin)
admin.site.register(Mecanico)
admin.site.register(Coche)
admin.site.register(Reparacion)