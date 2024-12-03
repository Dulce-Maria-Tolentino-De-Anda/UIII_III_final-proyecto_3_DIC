from django.db import models

# Create your models here.
class Ventas(models.Model):
    id_venta=models.PositiveIntegerField(primary_key=True)
    id_empleado=models.PositiveIntegerField()
    id_producto=models.PositiveIntegerField()
    id_cliente=models.PositiveIntegerField()
    fecha_venta=models.DateField(null=False,blank=False)
    cantidad=models.PositiveIntegerField()
    total=models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.id_venta