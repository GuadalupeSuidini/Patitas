from django.db import models


# Create your models here.
class usuarios(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    direccion = models.CharField(max_length=30)
    nacimiento = models.DateField()
    pais = models.CharField(max_length=20)
    departamento = models.CharField(max_length=20)
    celular = models.IntegerField()
    entidad = models.CharField(max_length=50)
    imagen = models.ImageField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido}"

class mascotas(models.Model):

    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    edad = models.DateField()
    vacunas = models.TextField(max_length=150)
    descripcion = models.TextField(max_length=150)
    imagen = models.ImageField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.nombre}'
    