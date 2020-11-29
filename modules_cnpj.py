import re
from random import randint


def remove_caracters(cnpj):
    cnpj = str(cnpj)
    return re.sub(r'[^0-9]', '', cnpj)


def check_cnpj(cnpj):
    cnpj = remove_caracters(cnpj)
    try:
        if is_sequential(cnpj):
            return False
    except:
        return False

    try:
        new_cnpj = create_digit(cnpj=cnpj, digit=1)
        new_cnpj = create_digit(cnpj=new_cnpj, digit=2)
    except Exception as exc:
        return False

    if new_cnpj == cnpj:
        return True
    else:
        return False


def create_digit(cnpj, digit):
    if digit == 1:
        regressive = LOOP[1:]
        new_cnpj = cnpj[:-2]
    elif digit == 2:
        regressive = LOOP
        new_cnpj = cnpj
    else:
        return None

    total = 0

    for index, sequence in enumerate(regressive):
        total += int(cnpj[index]) * sequence

    digit = 11 - (total % 11)
    digit = digit if digit <= 9 else 0

    return f'{new_cnpj}{digit}'


def is_sequential(cnpj):
    sequential = cnpj[0] * len(cnpj)
    if sequential == cnpj:
        return True
    else:
        return False


def new_cnpj_generator():
    cnpj = str(randint(10000000, 99999999))  # randint is generating the first 9 digits
    cnpj += '0001'

    cnpj_initial = f'{cnpj}00'  '''this variable is concatenating the first 12 digits +
                                   the 2 last digits that will be create by the function create_digit()'''

    new_cnpj = create_digit(cnpj=cnpj_initial, digit=1)  # Generating the first digit
    new_cnpj = create_digit(cnpj=new_cnpj, digit=2)  # Generating the first digit

    return new_cnpj


def format_cnpj(cnpj):
    cnpj = remove_caracters(cnpj)
    formatted = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
    return formatted


LOOP = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
