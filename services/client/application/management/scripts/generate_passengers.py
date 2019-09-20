from tqdm import tqdm

from application.management.scripts.date_utils import generate_random_time
from application.models import Passenger
from application.management.scripts.generate_people import generate_person
from application.management.scripts.generate_locations import generate_location


def generate_passenger():
    try:
        passenger = Passenger()
        generate_person(passenger)
        passenger.destination = generate_location()
        passenger.home_address = generate_location()
        passenger.entry_time = generate_random_time(type=0)     # tipo 0 = gera com horas de entrada (de 6h a 10h)
        passenger.exit_time = generate_random_time(type=1)      # tipo 1 = gera com horas de entrada (de 6h a 10h)
        passenger.status = 1
        passenger.save()

        return passenger

    except Exception as e:
        print("Exceção ao tentar gerar passageiro: ", e)
        return None


def generate_passengers(amount=100):
    for _ in tqdm(range(0, amount)):
        generate_passenger()
