from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    cantidad = models.IntegerField(default=0)
    fecha_creacion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Create your models here.
