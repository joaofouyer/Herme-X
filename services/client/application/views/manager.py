from django.shortcuts import render
from application.models import Manager


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
        managers = Manager.objects.all()
        return render(request, 'manager/list.html', {"managers": managers})

    except Exception as e:
        print("Exceção ao tentar listar todos os administradores: ", e)
        return True
