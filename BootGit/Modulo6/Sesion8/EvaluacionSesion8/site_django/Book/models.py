from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    valora = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
