from django.shortcuts import render

from application.functions import create_cluster_layer, create_stop_layer
from application.models import Route
from application.models import Passenger
from application.webservices.clustering import cluster_passengers
from application.webservices.location import find_nearest_stop


def list(request):
    try:
        routes = Route.objects.all()
        return render(request, 'line/list.html', {"lines": routes})

    except Exception as e:
        print("Exceção ao tentar listar as rotas: ", e)
        return True


def passengers_map(request):
    try:
        # TODO: Adicionar os passageiros na sessão
        return render(request, 'line/map.html')

    except Exception as e:
        print("Exceção ao tentar renderizar os passageiros no mapa: ", e)
        return True


def cluster(request):
    try:
        coordinates = []
        passengers = Passenger.objects.all()

        for p in passengers:
            coordinates.append([p.home_address.coordinates.latitude, p.home_address.coordinates.longitude])
        clusters = cluster_passengers(coordinates=coordinates)
        request.session['clusters'] = clusters
        request.session.modified = True
        create_cluster_layer(clusters['clusters'])
        return render(request, 'line/cluster.html')

    except Exception as e:
        print("Exceção ao tentar renderizar os passageiros no mapa: ", e)
        return True


def route_nearest_stop(request):
    try:
        clusters = request.session['clusters']
        stops = []
        for cluster in clusters['clusters']:
            stops.append(find_nearest_stop(coordinates=cluster))
        create_stop_layer(stops)
        return render(request, 'line/stop.html')

    except Exception as e:
        print("Exceção ao tentar renderizar os passageiros no mapa: ", e)
        return True
