from django.urls import path
from application.views.stop import *

urlpatterns = [
    path('', show_on_map, name='list_stops'),
]
