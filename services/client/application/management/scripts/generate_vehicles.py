from random import choice, randint
from string import ascii_uppercase
from application.models import Vehicle,Company
from application.management.scripts.generate_locations import generate_location

MODELS = ("Renault Master", "Caio Midi", "Caio Millennium Articulado", "Caio SoulClass", "Caio Solar 3200",
          "Mercedes-Benz Sprinter", "Caio Millennium BRT - Articulado", "Caio F2200", "Caio F2400", "Caio Foz Super",
          "Marcopolo Senior", "Citröen Jumper", "Caio Millennium BRT - Biarticulado", "Marcopolo Viaggio 900",
          "Marcopolo Viaggio 1050", "Marcopolo Viale", "Volkswagen Kombi", "Marcopolo New G7 1050",
          "Marcopolo New G7 1200", "Marcopolo Paradiso New G7 1350", "Marcopolo Torino", "Fiat Ducato",
          "Peugeout Boxer Minibus")


def generate_vehicle():
    try:
        company = Company.objects.first()
        license_plate = "{}{}{}{}{}{}{}".format(
            choice(ascii_uppercase), choice(ascii_uppercase), choice(ascii_uppercase), randint(0, 9), randint(0, 9),
            randint(0, 9), randint(0, 9))
        model = choice(MODELS)
        vehicle = Vehicle(
            status=1, model=model, capacity=randint(13, 42),
            address=company, license_plate=license_plate, name="{} / {}".format(license_plate, model)
        )
        return vehicle

    except Exception as e:
        print("Exceção ao tentar gerar veículo: ", e)
        return None


def generate_vehicles(amount=42):
    for _ in range(0, amount):
        generate_vehicle()
