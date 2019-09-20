from django.contrib import admin
from application.models.passenger import Passenger


class PassengerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Passenger, PassengerAdmin)
