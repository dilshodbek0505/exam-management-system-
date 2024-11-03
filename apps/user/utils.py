import random, string


def verification_code(k=6):
    return ''.join(random.choices(string.digits, k=k))
