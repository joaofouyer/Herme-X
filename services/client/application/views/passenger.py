from django.shortcuts import render

from application.models import Passenger


def create(request):
    pass


def get(request):
    pass


def update(request):
    pass


def delete(request):
    pass


def list(request):
    try:
        passengers = Passenger.objects.all()
        print(passengers.count())
        return render(request, 'passenger/list.html')

    except Exception as e:
        print("Exceção ao tentar listar todos os passageiros: ", e)
        return True
