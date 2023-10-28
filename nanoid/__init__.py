# coding: utf-8

from functools import reduce
from operator import concat

import random
import secrets
import string

alphabet_std = f"_-{string.digits}{string.ascii_letters}"
# alphabet_std = "_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_hum = "_-23456789abcdefghijkmnpqrstuvwxyzABCDEFGHIJKMNPQRSTUVWXYZ"

default_size = 21


def non_secure_generate(alphabet=alphabet_std, size=default_size):    
    return reduce(concat, (random.choice(alphabet) for _ in range(size)))


def generate(alphabet=alphabet_std, size=default_size):
    return reduce(concat, (secrets.choice(alphabet) for _ in range(size)))


__all__ = ["generate", "non_secure_generate", "alphabet_std", "alphabet_hum"]
