from django.db import models


class Geocoordinates(models.Model):
    class Meta:
        ordering = ['pk']
    coordinates = models.ForeignKey('Coordinates', on_delete=models.CASCADE, blank=False, null=False)
    geometry = models.ForeignKey('Geometry', on_delete=models.CASCADE, blank=False, null=False)
