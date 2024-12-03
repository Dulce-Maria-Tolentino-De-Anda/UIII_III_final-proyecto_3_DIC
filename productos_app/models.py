from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto=models.PositiveIntegerField(primary_key=True)
    modelo=models.CharField(max_length=100)
    tipo_camara=models.CharField(max_length=300)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    resolucion_mp=models.CharField(max_length=300)
    fecha_agregada=models.DateField()

    def __str__(self):
        return self.modelo