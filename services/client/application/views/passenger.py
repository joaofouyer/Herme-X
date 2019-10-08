from django.shortcuts import render
from application.models import Passenger, Stop, Location, Coordinates
from application.webservices.location import find_nearest_stop
from application.webservices.clustering import generate_locations


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
        return render(request, 'passenger/list.html', {"passengers": passengers})

    except Exception as e:
        print("Exceção ao tentar listar todos os passageiros: ", e)
        return True


def find_passenger_nearest_stop(passenger):
    from application.functions import get_address_boundaries, haversine

    try:
        origin_lat_range, origin_lng_range = get_address_boundaries(
            coordinates=passenger.home_address.get_coordinates(),
            degrees=0.002
        )
        destination_lat_range, destination_lng_range = get_address_boundaries(
            coordinates=passenger.destination.get_coordinates(),
            degrees=0.002
        )

        boarding = Stop.objects.filter(
            address__coordinates__latitude__range=origin_lat_range,
            address__coordinates__longitude__range=origin_lng_range
        )
        nearest = {
            "distance": float("inf"),
            "stop": None
        }

        for stop in boarding:
            distance = haversine(passenger.home_address.coordinates, stop.address.coordinates)
            if distance < nearest["distance"]:
                nearest['distance'] = distance
                nearest['stop'] = stop

    except Exception as e:
        print("Error on finding nearest stop :  {} {}".format(type(e), e))
        raise e


def generate_passenger_locations():
    try:
        center = [-23.658146, -46.771288]
        addresses = generate_locations(center=center, samples=6)
        passenger_id = 594
        for a in addresses:
            coord = Coordinates.handler(dictionary=a['coordinates'])
            coord.save()
            location = Location.handler(dictionary=a)
            location.coordinates = coord
            location.save()
            p = Passenger.objects.get(pk=passenger_id)
            p.home_address = location
            p.save()
            passenger_id = passenger_id + 1

        return False
    except Exception as e:
        print("Error on generating passengers locations:  {} {}".format(type(e), e))
        raise e
