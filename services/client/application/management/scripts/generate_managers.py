from datetime import date
from application.models import Manager, Person, Company
from application.management.scripts.generate_locations import generate_location
from application.management.scripts.cpf_utils import generate_cpf


def generate_managers():
    try:
        people = (
            Person(first_name="João", last_name="Fouyer", email="jfouyer@gmail.com", cpf="12845625731",
                   birthday=date(1997, 5, 22), phone="11953355055"),
            Person(first_name="Caroline", last_name="Appolinario", email="carolineappolinario@gmail.com",
                   cpf=generate_cpf(),
                   birthday=date(1995, 12, 31), phone="1199999999"),
            Person(first_name="Hector", last_name="Rauer", email="hectorrauer@gmail.com",
                   cpf=generate_cpf(),
                   birthday=date(1995, 9, 14), phone="1199999999"),
            Person(first_name="Elder", last_name="Nakashima", email="eldernakashima@gmail.com",
                   cpf=generate_cpf(),
                   birthday=date(1989, 3, 14), phone="1199999999"),
            Person(first_name="Reginaldo", last_name="Arakaki", email="rarakaki@scopus.com.br",
                   cpf=generate_cpf(),
                   birthday=date(1980, 9, 8), phone="1199999999"),
                  )
        bradesco = Company(name="Bradesco", email="inovabra@bradesco.com", cnpj="60746948000112",
                           address=generate_location(), phone="1125234252")
        bradesco.save()
        for person in people:
            manager = Manager(
                first_name=person.first_name, last_name=person.last_name, email=person.email, cpf=person.cpf,
                birthday=person.birthday, phone=person.phone)
            manager.status = 1
            manager.company = bradesco
            manager.home_address = generate_location()
            manager.save()

        return False

    except Exception as e:
        print("Exceção ao tentar gerar funcionários: ", e)
        return None
