from django.db import models
from application.models.person import Person


class Driver(Person):
    class Meta:
        ordering = ['pk']

    STATUS = (
        (0, 'inactive'),
        (1, 'active'),
        (2, 'vacation')
    )

    cnh = models.CharField(null=False, blank=False, max_length=15)
    status = models.IntegerField(default=0, null=False, blank=False, choices=STATUS)
    home_address = models.ForeignKey('Location', related_name='driver_home_address', null=False, blank=False,
                                     on_delete=models.PROTECT)

    def __str__(self):
        return "{first} {last}".format(first=self.first_name, last=self.last_name)
