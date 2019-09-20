from django.shortcuts import render
from application.models import Vehicle


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
        vehicles = Vehicle.objects.all()
        return render(request, 'vehicle/list.html', {"vehicles": vehicles})

    except Exception as e:
        print("Exceção ao tentar listar todos os veículos: ", e)
        return True
