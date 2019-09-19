from django.db import models
from application.models.person import Person
from django.utils import timezone


class User(Person):
    class Meta:
        db_table = 'client'

    STATUS = (
        (0, 'other'),
        (1, 'passenger'),
        (2, 'driver'),
        (3, 'manager')
    )

    type = models.IntegerField(choices=STATUS, default=0, blank=False, null=False)
    last_login = models.DateTimeField(default=timezone.now, blank=True)
    password = models.CharField(max_length=1023, blank=True, null=True)
    company = models.ForeignKey('Company', null=True, blank=True, on_delete=models.PROTECT)
    passenger = models.ForeignKey('Passenger', null=True, blank=True, on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', null=True, blank=True, on_delete=models.CASCADE)
    manager = models.ForeignKey('Manager', null=True, blank=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    token = models.ForeignKey('Token', related_name='session_token', null=False, blank=False, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.last_name, self.company.name)
