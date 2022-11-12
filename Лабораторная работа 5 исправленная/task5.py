import string
from random import sample


def get_random_password(n=8) -> str:  # TODO написать функцию генерации случайных паролей
    password = sample(list(string.ascii_lowercase + string.ascii_uppercase + string.digits), n)
    return ''.join(password)


print(get_random_password())
