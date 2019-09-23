from django.db import models


class RoutePath(models.Model):
    class Meta:
        ordering = ['pk']

    geometry = models.ForeignKey('Geometry', blank=False, null=False, on_delete=models.PROTECT)
