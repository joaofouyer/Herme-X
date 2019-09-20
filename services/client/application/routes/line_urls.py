from django.urls import path
from application.views.passenger import *
from application.views.line import *

urlpatterns = [
    path('', list, name='list_lines'),
]
