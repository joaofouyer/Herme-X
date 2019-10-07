from django.db import models


class Geometry(models.Model):
    class Meta:
        ordering = ['pk']

    TYPE = (
        (0, "Other"),
        (1, "Boundaries"),
        (2, "Route Shape")
    )

    type = models.IntegerField(default=0, blank=False, null=False, choices=TYPE)

    def json(self):
        try:

            return {
                "type": self.type,
                "id": self.id
            }

        except Exception as e:
            print("Exception on Geomtry json: {} {}".format(type(e), e))
            raise e
