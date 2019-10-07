from django.db import models
from application.models.coordinates import Coordinates
from application.models.geometry import Geometry


class Geocoordinates(models.Model):
    class Meta:
        ordering = ['pk']
    coordinates = models.ForeignKey('Coordinates', on_delete=models.CASCADE, blank=False, null=False)
    geometry = models.ForeignKey('Geometry', on_delete=models.CASCADE, blank=False, null=False)

    def json(self):
        try:

            return {
                "id": self.id,
                "coordinates": self.coordinates.json(),
                "geometry": self.geometry.json()
            }

        except Exception as e:
            print("Exception on Geocoordinates json: {} {}".format(type(e), e))
            raise e
