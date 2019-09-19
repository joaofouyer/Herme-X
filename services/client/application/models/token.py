from django.db import models
from django.utils import timezone


class Token(models.Model):
    class Meta:
        db_table = 'token'

    PERMISSIONS = (
        (0, 'passenger'),
        (1, 'driver'),
        (2, 'manager'),
        (3, 'all-access'),

    )

    permission = models.IntegerField(choices=PERMISSIONS, default=0)
    value = models.CharField(max_length=511, blank=True, null=True)
    created = models.DateTimeField(blank=False, null=False, default=timezone.now)
    expiry = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.value
