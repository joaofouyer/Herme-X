from django.core.management.base import BaseCommand, CommandError
from application.models import Passenger, Driver, Manager, Vehicle
from application.management.scripts import sptrans_to_json


class Command(BaseCommand):
    help = "Este comando converte os pontos da SPTrans!"

    def handle(self, *args, **options):
        try:
            sptrans_to_json()

        except Exception as e:
            raise CommandError('Não foi possível converter os pontos da SPTrans: ', e)
