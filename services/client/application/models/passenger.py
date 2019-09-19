from django.db import models
from django.utils import timezone
from application.models.person import Person


class Passenger(Person):
    class Meta:
        ordering = ['pk']

    STATUS = (
        (0, 'inactive'),
        (1, 'active'),
        (2, 'vacation')
    )

    destination = models.ForeignKey('Location', related_name='destination_address', null=False, blank=False,
                                    on_delete=models.PROTECT)
    entry_time = models.TimeField(blank=False, null=False, default=timezone.now)
    exit_time = models.TimeField(blank=False, null=False, default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=True, null=False, blank=False)
    password = models.CharField(blank=False, null=False, max_length=1023)
    home_address = models.ForeignKey('Location', related_name='passenger_home_address', null=False, blank=False,
                                     on_delete=models.PROTECT)

    def __str__(self):
        return "{first} {last}".format(first=self.first_name, last=self.last_name)
