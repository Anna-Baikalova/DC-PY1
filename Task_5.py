import string
import random

def get_random_password() -> str:
    ...  # TODO написать функцию генерации случайных паролей
    vals = ''.join(string.ascii_letters) + string.digits
    l = random.sample(vals, 8)
    return ''.join(x for x in l)

print(get_random_password())
