import random


def generate_cpf():
    try:
        c = "".join(i for i in [str(random.randint(0, 9)) for _ in range(0, 9)])
        cpf = "{}{}".format(c, calc_cpf_digits(c))
        return cpf

    except Exception as e:
        print("Exceção no método generate_cpf: ", e)
        return None


def verify_cpf_digit(cpf):
    try:
        cpf = cpf if isinstance(cpf, str) else str(cpf)
        cpf = cpf.replace('.', '').replace('-', '')
        return str(calc_cpf_digits(cpf[:9])) == cpf[9:] if len(cpf) == 11 else False

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
