class Fabricante(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre

