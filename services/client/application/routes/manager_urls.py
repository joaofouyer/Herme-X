from django.urls import path
from application.views.manager import *

urlpatterns = [
    path('', list, name='list_managers'),
]
