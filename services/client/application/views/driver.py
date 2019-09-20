from django.shortcuts import render
from application.models import Driver


def create(request):
    pass


def retrieve(request):
    pass


def update(request):
    pass


def delete(request):
    pass


def list(request):
    try:
        drivers = Driver.objects.all()
        return render(request, 'driver/list.html', {"drivers": drivers})

    except Exception as e:
        print("Exceção ao tentar listar todos os motoristas: ", e)
        return True
