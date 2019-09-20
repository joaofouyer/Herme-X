import random
from tqdm import tqdm
import unidecode
from datetime import datetime
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

from application.models import Location, Coordinates
from application.models.passenger import Passenger


FIRST_NAME = ["João", "Elder", "Caroline", "Hector", "Carlos", "Eduardo", "Reginaldo", "Julio", "Lídia", "Daniel",
              "Gabriel", "Gustavo", "Guilherme", "Amanda", "Bianca", "Brenda", "Bruna", "Bruno", "Lisbete", "Maria",
              "Inês", "Mary", "Ângela", "Mariana", "Mariane", "Júlia", "Cristiana", "Italo", "José", "Catarina",
              "André", "Leandro", "Fábio", "Fabiana", "Luana", "Carla", "Mirella", "Thais", "Cristina", "Lupita",
              "Stefany", "Lourdes", "Giovana", "Edith", "Cícero", "Jayme", "Arthur", "Victor", "Daniel", "Daniela"]

LAST_NAME = ["Fouyer", "Arakaki", "Vega", "Paes", "Santiago", "Madsen", "Preto", "Bayonna", "Medeiros", "Ranzini",
             "Barbosa", "Lima", "Rauer", "Appolinario", "Santos", "Silva", "Jesus", "Oliveira", "Magalhães", "França",
             "Rodrigues", "Machado", "Assis", "Pessoa", "Turgin", "Da Vinci", "Jobs", "Gates", "Klein", "Nakashima"]


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
                location = Location.objects.first()
                if not location:
                    coordinates = Coordinates(latitude=-23.554189, longitude=-46.662206)
                    coordinates.save()
                    location = Location(
                        street="Av. Angélica",
                        street_number=2529,
                        info="inovabra habitat",
                        neighborhood="Bela Vista",
                        city="São Paulo",
                        state="SP",
                        country="BR",
                        zip_code="01227200",
                        coordinates=coordinates
                    )
                    location.save()
                for p in tqdm(range(0, 100)):
                    passenger = Passenger()
                    passenger.destination = location
                    passenger.home_address = location
                    passenger.entry_time = datetime.strptime(
                        "2019-05-22 {}:{}:00".format(random.randint(6, 9), random.randint(0, 59)),
                        "%Y-%m-%d %H:%M:%S"
                    ).time()

                    passenger.exit_time = datetime.strptime(
                        "2019-05-22 {}:{}:00".format(random.randint(13, 21), random.randint(0, 59)),
                        "%Y-%m-%d %H:%M:%S"
                    ).time()

                    passenger.status = 1

                    passenger.first_name = FIRST_NAME[random.randint(0, len(FIRST_NAME)-1)]
                    passenger.last_name = LAST_NAME[random.randint(0, len(LAST_NAME)-1)]
                    if random.randint(0, 1):
                        passenger.last_name = "{} {}".format(passenger.last_name, LAST_NAME[random.randint(0, len(LAST_NAME)-1)])

                    passenger.email = "{first}{last}@brades.co".format(
                        first=unidecode.unidecode(passenger.first_name.lower().replace(' ', '')),
                        last=unidecode.unidecode(passenger.last_name.lower().replace(' ', '')))

                    passenger.phone = str(random.randint(11900000000, 11999999999))

                    passenger.birthday = datetime.strptime(
                        "{y}-{m}-{d}".format(y=random.randint(1960, 2001), m=random.randint(1, 12), d=random.randint(1, 28)),
                        "%Y-%m-%d"
                    ).date()
                    passenger.cpf = generate_cpf()
                    passenger.created = timezone.now()
                    passenger.save()

        except Exception as e:
            raise CommandError('Não foi criar datasets: ', e)


def generate_cpf():
    try:
        c = ""
        for i in range(0, 9):
            c = c + str(random.randint(0, 9))
        cpf = "{}{}".format(c, calc_cpf_digits(c))
        return cpf

    except Exception as e:
        print("Exceção no método generate_cpf: ", e)
        return None


def verify_cpf_digit(cpf):
    try:
        cpf = cpf if isinstance(cpf, str) else str(cpf)
        cpf = cpf.replace('.', '').replace('-', '')
        if len(cpf) == 11:
            if str(calc_cpf_digits(cpf[:9])) == cpf[9:]:
                return True
        return False

    except Exception as e:
        print("Exceção no método verify_cpf_digit: ", e)
        return None


def calc_cpf_digits(cpf):
    try:
        cpf = cpf.replace('.', '').replace('-', '')
        if len(cpf) == 9:
            first = 0
            for i in range(0, 9):
                first = first + int(cpf[i]) * (i + 1)
            first = first % 11
            second = 0
            for i in range(1, 9):
                second = second + int(cpf[i]) * i
            second = (second + first * 9) % 11

            return "{}{}".format(first, second)
        else:
            print("Para calcular os dois dígitos verificadores do CPF, forneça apenas os nove primeiros dígitos.")
            return None

    except Exception as e:
        print("Exceção no método calc_cpf_digit: ", e)
        return None
