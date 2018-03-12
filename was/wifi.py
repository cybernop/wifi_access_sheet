import random
import string


def gen_password(length, write=False):
    password = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))
    if write:
        with open('password.txt', 'w') as file:
            file.write(password)
    return password
