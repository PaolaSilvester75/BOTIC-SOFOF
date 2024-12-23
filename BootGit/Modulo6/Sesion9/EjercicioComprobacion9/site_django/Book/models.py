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