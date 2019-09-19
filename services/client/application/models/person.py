import datetime
from django.db import models
from django.utils import timezone


class Person(models.Model):
    class Meta:
        abstract = True
        ordering = ['pk']

    first_name = models.CharField(max_length=127, blank=False, null=False)
    last_name = models.CharField(max_length=127, blank=False, null=False)
    email = models.CharField(max_length=127, blank=False, null=False)
    cpf = models.CharField(max_length=15, blank=False, null=False)
    birthday = models.DateField(blank=False, null=False,
                                default=datetime.datetime.strptime("1997-05-22", "%Y-%m-%d").date())
    phone = models.CharField(max_length=15, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False, default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{first} {last}".format(first=self.first_name, last=self.last_name)
