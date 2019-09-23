from django.db import models


class Zone(models.Model):
    class Meta:
        ordering = ['pk']

    TYPES = (
        (0, "Other"),
        (1, "Uber Movement")
    )

    type = models.IntegerField(default=0, choices=TYPES, blank=False, null=False)
    name = models.CharField(max_length=127, blank=False, null=False)
    number = models.IntegerField(blank=True, null=False)
    district_name = models.CharField(max_length=127, blank=True, null=True)
    district_number = models.IntegerField(blank=True, null=True)
    city_name = models.CharField(max_length=127, blank=True, null=True)
    city_number = models.IntegerField(blank=True, null=True)
    movement_id = models.CharField(max_length=127, blank=True, null=True)
    geometry = models.ForeignKey('Geometry', related_name='zone_geometry', null=True, blank=True,
                                 on_delete=models.PROTECT)

    def __str__(self):
        return self.name

