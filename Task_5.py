import string
from random import sample

def get_random_password(n=8) -> str:
    symbols = string.ascii_letters + string.digits  # TODO написать функцию генерации случайных паролей
    password = sample(symbols, n)
    password = ''.join(password)
    return password

print(get_random_password())
