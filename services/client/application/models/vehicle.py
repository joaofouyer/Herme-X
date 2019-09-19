from django.db import models


class Vehicle(models.Model):
    class Meta:
        ordering = ['pk']

    STATUS = (
        (0, 'inactive'),
        (1, 'active'),
        (2, 'maintenance')
    )

    name = models.CharField(max_length=127, blank=False, null=False)
    model = models.CharField(max_length=127, blank=False, null=False)
    license_plate = models.CharField(max_length=15, blank=False, null=False)
    capacity = models.IntegerField(null=False, blank=False, default=13)
    address = models.ForeignKey('Company', related_name='vehicle_company', null=True, blank=True,
                                on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, blank=False, null=False, default=True)

    def __str__(self):
        return self.name
