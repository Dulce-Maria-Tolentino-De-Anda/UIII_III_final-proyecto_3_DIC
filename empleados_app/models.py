from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    direccion=models.CharField(max_length=255)
    telefono=models.PositiveIntegerField()
    email=models.CharField(max_length=100)
    fecha_nacimiento=models.DateField(null=False,blank=False)
    
    def __str__(self):
        return self.nombre