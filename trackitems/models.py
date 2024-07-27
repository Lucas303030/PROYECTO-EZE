from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Pieza(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Tracking(models.Model):
    ESTADO = (
    ("Arribado", "Arribado"),
    ("Demorado", "Demorado"),
    ("En transito", "En transito")
)
    pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    Fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    origen = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    estado= models.CharField(max_length=50, choices=ESTADO)  # opciones: 'en transito', 'arribado', 'demorado'

    def __str__(self):
        return f"{self.pieza.nombre} - {self.estado}"