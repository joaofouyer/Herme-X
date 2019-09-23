from django.core.management.base import BaseCommand, CommandError
from application.management.scripts import import_movement_zones


class Command(BaseCommand):
    help = "Este comando importa as zonas do Uber Movement!"

    def handle(self, *args, **options):
        try:
            import_movement_zones()

        except Exception as e:
            raise CommandError('Não foi possível importar as Zonas do Uber Movement: ', e)
