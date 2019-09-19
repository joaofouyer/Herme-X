from django.urls import path
from application.views.index import *

urlpatterns = [
    path('', index, name='index'),
]
