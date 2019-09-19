from django.urls import path
from application.views.passenger import *

urlpatterns = [
    path('', list, name='list_passengers'),
]
