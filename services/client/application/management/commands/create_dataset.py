from django.core.management.base import BaseCommand, CommandError
from application.models import Passenger, Driver, Manager, Vehicle, Zone, Stop
from application.management.scripts import generate_passengers, generate_drivers, generate_managers, generate_vehicles, \
    import_movement_zones, import_stops


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

            zones_count = Zone.objects.all().count()

            if zones_count:
                self.stdout.write("Como já existe(m) {} zonas criadas, a etapa de criação "
                                  "será pulada.\n".format(zones_count))

            else:
                self.stdout.write("Importanto zonas de São Paulo do Uber Movement. Sente-se e pegue um café.\n")
                import_movement_zones()

            stops_count = Stop.objects.all().count()

            if stops_count:
                self.stdout.write("Como já existe(m) {} pontos criados, a etapa de criação "
                                  "será pulada.\n".format(stops_count))

            else:
                self.stdout.write("Importanto pontos da SPTrans.\n")
                import_stops()

        except Exception as e:
            raise CommandError('Não foi possível criar datasets: ', e)
