from django.db import models
from application.models import Location
from application.models import Company


class Stop(models.Model):
    class Meta:
        ordering = ['pk']

    TYPE_CHOICES = (
        (0, 'other'),
        (1, 'totem'),
        (2, 'roof')
    )

    SIDEWALK_CHOICES = (
        (0, 'other'),
        (1, 'sidewalk'),
        (2, 'lane')
    )

    address = models.ForeignKey(Location, related_name='stop_address', null=False, blank=False,
                                on_delete=models.PROTECT)
    reference = models.CharField(max_length=127, blank=True, null=True)
    type = models.IntegerField(default=0, choices=TYPE_CHOICES, blank=False, null=False)
    sidewalk = models.IntegerField(default=0, choices=SIDEWALK_CHOICES, blank=False, null=False)
    company = models.ForeignKey(Company, related_name='stop_company', null=True, blank=True, on_delete=models.PROTECT)

    def coordinates(self):
        return self.address.get_coordinates()

    def __str__(self):
        if self.reference:
            return "Parada -> {r}".format(r=self.reference)
        else:
            return "Parada -> {r}".format(r=self.address.__str__())

    def json(self):
        try:

            return {
                "id": self.id,
                "address": {
                    "id": self.address.id,
                    "coordinates": {
                        "latitude": self.address.coordinates.latitude,
                        "longitude": self.address.coordinates.longitude
                    }
                },
                "reference": self.reference,
                "type": self.type,
                "sidewalk": self.sidewalk,
                "company_id": 0
            }

        except Exception as e:
            print("Exception on Stop json: {} {}".format(type(e), e))
            raise e
