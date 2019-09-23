from django.db import models


class Location(models.Model):
    class Meta:
        ordering = ['coordinates']

    street = models.CharField(max_length=127, blank=False, null=False)
    street_number = models.IntegerField(blank=True, null=False)
    info = models.CharField(max_length=127, blank=False, null=False)
    neighborhood = models.CharField(max_length=127, blank=True, null=True)
    city = models.CharField(max_length=127, blank=True, null=True)
    state = models.CharField(max_length=3, blank=True, null=True)
    country = models.CharField(max_length=3, blank=True, null=True)
    zip_code = models.CharField(max_length=15, blank=True, null=True)
    coordinates = models.ForeignKey('Coordinates', related_name='address_coordinates', null=True, blank=True,
                                    on_delete=models.PROTECT)
    zone = models.ForeignKey('Zone', related_name='address_zone', null=True, blank=True,
                             on_delete=models.PROTECT)

    def __str__(self):
        return "{s}, {sn} - {n}, {c} - {state}, {zc} ({info})".format(
            s=self.street, sn=self.street_number, n=self.neighborhood, c=self.city, state=self.state, zc=self.zip_code,
            info=self.info)

    def get_coordinates(self):
        return self.coordinates.__str__()
