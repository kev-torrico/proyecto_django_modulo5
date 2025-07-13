from django.core.exceptions import ValidationError
from django.utils import timezone

def salario_minimo(value):
    if value<2500:
        raise ValidationError("El salario minimo no puede ser menor a 2500 bs.")
    
def horas_trabajadas(value):
    if value<=0 or value>8:
        raise ValidationError("Las horas trabajadas deben estar entre 1 y 8 horas laborales diarias")
    
def fecha_reparacion(value):
    if value< timezone.localdate():
        raise ValidationError("La fecha de reparación no debe ser anterior a la fecha actual")