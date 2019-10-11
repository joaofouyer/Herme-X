from django.shortcuts import render

from application.functions import create_cluster_layer, create_stop_layer
from application.models import Route
from application.models import Passenger
from application.webservices.clustering import cluster_passengers
from application.webservices.location import find_nearest_stop, sort_places
import datetime


def list(request):
    try:
        routes = Route.objects.all()
        return render(request, 'line/list.html', {"lines": routes})

    except Exception as e:
        print("Exceção ao tentar listar as rotas: ", e)
        return True


def passengers_map(request):
    try:
        request.session.flush()
        passengers = Passenger.objects.filter(status=1)
        passengers_dict = []
        for p in passengers:
            passengers_dict.append({
                "id": p.id,
                "origin": {
                    "latitude": p.home_address.coordinates.latitude,
                    "longitude": p.home_address.coordinates.longitude
                },
                "destination": {
                    "latitude": p.destination.coordinates.latitude,
                    "longitude": p.destination.coordinates.longitude
                },
                "times": {
                    "entry": p.entry_time.strftime("%H:%M"),
                    "exit": p.exit_time.strftime("%H:%M")

                }
            })
        request.session['passengers'] = passengers_dict
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
        print("Exceção ao tentar renderizar clusters no mapa: ", e)
        return True


def route_nearest_stop(request):
    try:
        passengers = request.session['passengers']
        passengers = find_nearest_stop(passengers=passengers)
        coordinates = create_stop_layer(passengers=passengers)
        request.session['coordinates'] = coordinates
        request.session.modified = True

        return render(request, 'line/stop.html')

    except Exception as e:
        print("Exception on line route_nearest_stop: {} {}".format(type(e), e))
        raise e


def sort_stops(request):
    try:
        clusters_stops = request.session['clusters_stops']

        sorted_stops = []
        for stops in clusters_stops:
            sorted = sort_places(places=stops)
            sorted_stops.append(sorted)
        print(sorted_stops)
        return render(request, 'line/sort.html')

    except Exception as e:
        print("Exception on line sort_stops: {} {}".format(type(e), e))
        raise e
