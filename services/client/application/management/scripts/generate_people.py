from random import randint, choice
import unidecode
from django.utils import timezone

from application.management.scripts.date_utils import generate_random_birthday
from application.management.scripts.cpf_utils import generate_cpf


FIRST_NAME = ("João", "Elder", "Caroline", "Hector", "Carlos", "Eduardo", "Reginaldo", "Julio", "Lídia", "Daniel",
              "Gabriel", "Gustavo", "Guilherme", "Amanda", "Bianca", "Brenda", "Bruna", "Bruno", "Lisbete", "Maria",
              "Inês", "Mary", "Ângela", "Mariana", "Mariane", "Júlia", "Cristiana", "Italo", "José", "Catarina",
              "André", "Leandro", "Fábio", "Fabiana", "Luana", "Carla", "Mirella", "Thais", "Cristina", "Lupita",
              "Stefany", "Lourdes", "Giovana", "Edith", "Cícero", "Jayme", "Arthur", "Victor", "Daniel", "Daniela")

LAST_NAME = ("Fouyer", "Arakaki", "Vega", "Paes", "Santiago", "Madsen", "Preto", "Bayonna", "Medeiros", "Ranzini",
             "Barbosa", "Lima", "Rauer", "Appolinario", "Santos", "Silva", "Jesus", "Oliveira", "Magalhães", "França",
             "Rodrigues", "Machado", "Assis", "Pessoa", "Turgin", "Da Vinci", "Jobs", "Gates", "Klein", "Nakashima")


def generate_person(person):
    try:
        person.first_name = choice(FIRST_NAME)
        person.last_name = choice(LAST_NAME)
        if randint(0, 1):
            person.last_name = "{} {}".format(person.last_name, choice(LAST_NAME))

        person.email = "{first}{last}@brades.co".format(
            first=unidecode.unidecode(person.first_name.lower().replace(' ', '')),
            last=unidecode.unidecode(person.last_name.lower().replace(' ', '')))

        person.phone = str(randint(11900000000, 11999999999))

        person.birthday = generate_random_birthday()
        person.cpf = generate_cpf()
        person.created = timezone.now()
        return person

    except Exception as e:
        print("Exceção ao tentar gerar pessoa: ", e)
        return None
