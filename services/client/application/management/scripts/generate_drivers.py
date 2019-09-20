from tqdm import tqdm
import random
from application.models import Driver
from application.management.scripts.generate_people import generate_person
from application.management.scripts.generate_locations import generate_location


def generate_driver():
    try:
        driver = Driver()
        generate_person(driver)
        driver.home_address = generate_location()
        driver.cnh = str(random.randint(1000000000, 9999999999))
        driver.status = random.randint(0, 2)
        driver.save()

        return driver

    except Exception as e:
        print("Exceção ao tentar gerar motorista: ", e)
        return None


def generate_drivers(amount=42):
    for _ in tqdm(range(0, amount)):
        generate_driver()
