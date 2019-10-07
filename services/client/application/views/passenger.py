from django.shortcuts import render
from application.models import Passenger, Stop
from application.webservices.location import find_nearest_stop


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
        passengers = Passenger.objects.all()
        p = passengers.first()
        coord = {
            "latitude": p.home_address.coordinates.latitude,
            "longitude": p.home_address.coordinates.longitude
        }
        coordinates = [coord]
        bla = find_nearest_stop(coordinates=coordinates)
        return render(request, 'passenger/list.html', {"passengers": passengers})

    except Exception as e:
        print("Exceção ao tentar listar todos os passageiros: ", e)
        return True


# def find_nearest_stop(passenger):
#     from application.functions import get_address_boundaries, haversine
#
#     try:
#         origin_lat_range, origin_lng_range = get_address_boundaries(
#             coordinates=passenger.home_address.get_coordinates(),
#             degrees=0.002
#         )
#         destination_lat_range, destination_lng_range = get_address_boundaries(
#             coordinates=passenger.destination.get_coordinates(),
#             degrees=0.002
#         )
#
#         boarding = Stop.objects.filter(
#             address__coordinates__latitude__range=origin_lat_range,
#             address__coordinates__longitude__range=origin_lng_range
#         )
#         nearest = {
#             "distance": float("inf"),
#             "stop": None
#         }
#
#         for stop in boarding:
#             distance = haversine(passenger.home_address.coordinates, stop.address.coordinates)
#             if distance < nearest["distance"]:
#                 nearest['distance'] = distance
#                 nearest['stop'] = stop
#
#     except Exception as e:
#         print("Error on finding nearest stop :  {} {}".format(type(e), e))
#         raise e

# from application.views.passenger import *