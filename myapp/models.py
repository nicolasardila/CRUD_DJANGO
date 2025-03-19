from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=45)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return self.nombre
