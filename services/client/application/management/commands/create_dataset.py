from django.core.management.base import BaseCommand, CommandError
from application.models import Passenger, Driver, Manager, Vehicle
from application.management.scripts.generate_passengers import generate_passengers
from application.management.scripts.generate_drivers import generate_drivers
from application.management.scripts.generate_managers import generate_managers
from application.management.scripts.generate_vehicles import generate_vehicles


class Command(BaseCommand):
    help = "Este comando cria massa de testes e realiza persistência na base de dados."

    def handle(self, *args, **options):
        try:
            passengers_count = Passenger.objects.all().count()
            if passengers_count:
                self.stdout.write("Como já existe(m) {} passageiros criados, a etapa de criação "
                                  "será pulada.\n".format(passengers_count))
            else:
                self.stdout.write("Criando Passageiros\n")
                generate_passengers(amount=100)

            drivers_count = Driver.objects.all().count()
            if drivers_count:
                self.stdout.write("Como já existe(m) {} motoristas criados, a etapa de criação "
                                  "será pulada.\n".format(drivers_count))
            else:
                self.stdout.write("Criando motoristas\n")
                generate_drivers(amount=42)

            managers_count = Manager.objects.all().count()
            if managers_count:
                self.stdout.write("Como já existe(m) {} funcionários criados, a etapa de criação "
                                  "será pulada.\n".format(managers_count))
            else:
                self.stdout.write("Criando funcionários\n")
                generate_managers()

            vehicles_count = Vehicle.objects.all().count()
            if vehicles_count:
                self.stdout.write("Como já existe(m) {} veículos criados, a etapa de criação "
                                  "será pulada.\n".format(vehicles_count))
            else:
                self.stdout.write("Criando veículos\n")
                generate_vehicles(42)

        except Exception as e:
            raise CommandError('Não foi possível criar datasets: ', e)
