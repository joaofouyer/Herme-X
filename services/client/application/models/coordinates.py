from django.db import models
from math import radians


class Coordinates(models.Model):
    class Meta:
        ordering = ['latitude', 'longitude']

    latitude = models.FloatField(default=-23.554189, blank=False, null=False)
    longitude = models.FloatField(default=-46.662206, blank=False, null=False)

    def __str__(self):
        return self.latitude, self.longitude

    def to_radians(self):
        return radians(self.latitude), radians(self.longitude)
