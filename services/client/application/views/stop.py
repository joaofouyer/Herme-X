from django.shortcuts import render
from application.models import Stop


def show_on_map(request):
    try:
        return render(request, 'stop/map.html')

    except Exception as e:
        print("Exceção ao tentar listar abrir mapa com todos os pontos: ", e)
        return True
