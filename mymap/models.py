from django.db import models

class Location(models.Model):
    Nombre = models.CharField(max_length=255)
    Descripcion = models.TextField()
    Lat = models.DecimalField(max_digits=9, decimal_places=6)
    Lng = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.Nombre