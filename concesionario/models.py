from django.db import models

# Create your models here.
class Cliente(models.Model):
    ci = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Mecanico(models.Model):
    ci = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class CocheTipo (models.TextChoices):
    NUEVO = "nuevo", "NUEVO"
    USADO = "usado", "USADO"

class Coche(models.Model):
    matricula = models.CharField(primary_key=True, max_length=20)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    tipo = models.CharField(
        max_length=5,
        choices=CocheTipo.choices,
        default=CocheTipo.NUEVO
    )
    unidades = models.PositiveBigIntegerField(null=True, blank=True)
    kilometros = models.PositiveBigIntegerField(null=True, blank=True)
    comprador = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.matricula}"

class Reparacion (models.Model):
    coche = models.ForeignKey(Coche, on_delete=models.CASCADE)
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    fecha_reparacion = models.DateField()
    horas_trabajo = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Reparacion del {self.coche} por {self.mecanico} el {self.fecha_reparacion}"