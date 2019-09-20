from django.urls import path
from application.views.driver import *

urlpatterns = [
    path('', list, name='list_drivers'),
]
