from django.db import models


class RouteStop(models.Model):
    class Meta:
        ordering = ['pk']

    TYPE = (
        (0, "Pick-up"),
        (1, "Drop-off")
    )

    type = models.IntegerField(default=0, blank=False, null=False, choices=TYPE)
    time = models.TimeField(blank=False, null=False)
    route = models.ForeignKey('Route', blank=False, null=False, on_delete=models.CASCADE)
    stop = models.ForeignKey('Stop', blank=False, null=False, on_delete=models.PROTECT)
