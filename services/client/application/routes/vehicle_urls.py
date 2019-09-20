from django.urls import path
from application.views.vehicle import *

urlpatterns = [
    path('', list, name='list_vehicles'),
]
