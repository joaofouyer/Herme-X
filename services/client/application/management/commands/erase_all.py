from django.core.management.base import BaseCommand, CommandError
from application.models import Zone, Geometry, Coordinates, Passenger, Driver, Vehicle, Manager, Person, Location, \
    Company


class Command(BaseCommand):
    help = "Este comando apaga tudo da sua base de dados"

    def handle(self, *args, **options):
        try:
            self.stdout.write("Apagando todos os funcionários!")
            [m.delete() for m in Manager.objects.all()]
            self.stdout.write("Apagando todos os veículos!")
            [v.delete() for v in Vehicle.objects.all()]
            self.stdout.write("Apagando todos os motoristas!")
            [d.delete() for d in Driver.objects.all()]
            self.stdout.write("Apagando todos os passageiros!")
            [p.delete() for p in Passenger.objects.all()]
            self.stdout.write("Apagando todas as zonas!")
            [z.delete() for z in Zone.objects.all()]
            self.stdout.write("Apagando todas as formas geométricas!")
            [g.delete() for g in Geometry.objects.all()]
            self.stdout.write("Apagando todas as empresas!")
            [c.delete() for c in Company.objects.all()]
            self.stdout.write("Apagando todos os endereços!")
            [l.delete() for l in Location.objects.all()]
            self.stdout.write("Apagando todas as coordenadas!")
            [c.delete() for c in Coordinates.objects.all()]

        except Exception as e:
            raise CommandError('Não foi possível apagar tudo: ', e)
