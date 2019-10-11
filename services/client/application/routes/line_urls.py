from django.urls import path
from application.views.line import *

urlpatterns = [
    path('', list, name='list_lines'),
    path('/passageiros', passengers_map, name='passengers_map'),
    path('/cluster', cluster, name='cluster'),
    path('/paradas', route_nearest_stop, name='find-nearest-stops'),
    path('/ordenado', sort_stops, name='sort-stops'),
]
