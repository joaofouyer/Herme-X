from django.core.management.base import BaseCommand, CommandError
from application.webservices.location import sync
from application.models import Coordinates, Geometry, Geocoordinates, Location, Zone, Stop


class Command(BaseCommand):
    help = "Este comando realiza o sync da base de dados do client com a base de dados do locations microservice."

    def handle(self, *args, **options):
        try:
            # Coordinates.
            # coordinates = Coordinates.objects.all()
            # coordinates = [c.json() for c in coordinates]
            # sync(mode="coordinates", data=coordinates)

            # # Geometry
            # geometries = Geometry.objects.all()
            # geometries = [g.json() for g in geometries]
            # sync(mode="shape", data=geometries)

            # # GeoCoordinates
            # start = 60000
            # while start < 100000:
            #     end = start + 5000
            #     geo = Geocoordinates.objects.filter(pk__range=[start, end])
            #     print("start: ", start, "count: ", geo.count())
            #     geo = [g.json() for g in geo]
            #     sync(mode="geocoordinates", data=geo)
            #     start = start + 5000

            # #Zone:
            # zones = Zone.objects.all()
            # print(zones.count())
            # zones = [z.json() for z in zones]
            # sync(mode="zone", data=zones)

            # Location
            # locations = Location.objects.all()
            # print(locations.count())
            # locations = [l.json() for l in locations]
            # sync(mode="location", data=locations)
            #
            # # Stop
            stops = Stop.objects.all()
            print(stops.count())
            stops = [s.json() for s in stops]
            sync(mode="stop", data=stops)

        except Exception as e:
            raise CommandError('Não foi possível sincronizar: ', e)
