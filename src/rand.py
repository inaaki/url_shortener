import random
from string import ascii_letters, digits


string = ascii_letters + digits


def get_id():
    return ''.join(random.choices(string, k=8))
