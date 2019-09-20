from random import randint
from datetime import datetime


def generate_random_time(type=0):
    """
    :param type: 0 para horário de entrada no trabalho/faculdade; 1 para horário de saída
    :return: objeto do tipo time
    """
    try:
        hour = randint(13, 20) if type else randint(6, 10)
        minute = randint(0, 59)
        return datetime.strptime("2019-05-22 {}:{}:00".format(hour, minute), "%Y-%m-%d %H:%M:%S").time()
    except Exception as e:
        print("Exceção ao tentar gerar horário: ", e)
        return None


def generate_random_birthday():
    return datetime.strptime(
        "{y}-{m}-{d}".format(y=randint(1960, 2001), m=randint(1, 12), d=randint(1, 28)), "%Y-%m-%d"
    ).date()
