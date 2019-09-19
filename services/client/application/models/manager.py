from django.db import models
from application.models.person import Person


class Manager(Person):
    class Meta:
        ordering = ['pk']

    STATUS = (
        (0, 'inactive'),
        (1, 'active'),
        (2, 'vacation')
    )

    company = models.ForeignKey('Company', related_name='manager_company', null=False, blank=False,
                                on_delete=models.PROTECT)
    status = models.IntegerField(default=0, null=False, blank=False, choices=STATUS)
    password = models.CharField(blank=False, null=False, max_length=1023)
    home_address = models.ForeignKey('Location', related_name='manager_home_address', null=False, blank=False,
                                     on_delete=models.PROTECT)

    def __str__(self):
        return "{first} {last}".format(first=self.first_name, last=self.last_name)
