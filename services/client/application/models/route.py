from django.db import models


class Route(models.Model):
    class Meta:
        ordering = ['pk']

    DIRECTION = (
        (0, "Other"),
        (1, "Go"),
        (2, "Back")
    )

    direction = models.IntegerField(default=0, blank=False, null=False, choices=DIRECTION)
    vehicle = models.ForeignKey('Vehicle', blank=False, null=False, on_delete=models.PROTECT)
    driver = models.ForeignKey('Driver', blank=False, null=False, on_delete=models.PROTECT)
    path = models.ForeignKey('RoutePath', blank=True, null=True, on_delete=models.PROTECT)
