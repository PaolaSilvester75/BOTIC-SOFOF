from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    valora = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        permissions = [
            ("development", "Permiso como Desarrollador"),
            ("scrum_master", "Permiso como Scrum Master"),
            ("product_owner", "Permiso como Product Owner"),
        ]

    def __str__(self):
        return self.title




class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    rating = models.FloatField(default=0)
    value = models.FloatField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def get_rating_category(self):
        if self.rating < 1000:
            return 'Baja'
        elif 1000 <= self.rating <= 2500:
            return 'Media'
        else:
            return 'Alta'


    def __str__(self):
        return f'{self.title} - {self.get_rating_category()}'

    class Meta:
        ordering = ['fecha_creacion']

