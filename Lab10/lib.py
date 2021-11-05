import random
import numpy as np

def gcd(a, b):
   
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


def xgcd(a, b):
    
    x, old_x = 0, 1
    y, old_y = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return a, old_x, old_y


def chooseE(phi):
   
    while (True):
        e = random.randrange(2, phi)

        if (gcd(e, phi) == 1):
            return e

def power(a, n, p):
    # Initialize result
    res = 1
    a = a % p 

    while n > 0:
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
            n = n // 2
    return res % p

def listJoiner(lista, caracter):
    if isinstance(lista, list):
        return caracter.join(map(str, lista))

    raise TypeError("El parámetro lista debe ser una lista")