from django.db import models
from django.utils import timezone


class Company(models.Model):
    class Meta:
        ordering = ['pk']

    name = models.CharField(max_length=127, blank=False, null=False)
    email = models.CharField(max_length=127, blank=False, null=False)
    cnpj = models.CharField(max_length=15, blank=False, null=False)
    address = models.ForeignKey('Location', related_name='company_address', null=False, blank=False,
                                on_delete=models.PROTECT)
    phone = models.CharField(max_length=15, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False, default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
