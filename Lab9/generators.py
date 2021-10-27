import random
import base64
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


def generate(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            if n % 2 != 0:
                prime_list.append(n)

    return prime_list


def generar_clave():

    p = (generate(200, 1000))
    p = np.random.choice(p)
    q = np.random.choice(p)
  
    n = p * q
    

    phi = (p - 1) * (q - 1)
    e = chooseE(phi)

    gcd, x, y = xgcd(e, phi)

    if (x < 0):
        d = x % phi
    else:
        d = x

    print('\n[CLAVES GENERADAS]\n')
    public = (str(e)+'.'+str(n)).encode('ascii')
    public = base64.b64encode(public).decode()
    f_public = open('public_keys.txt', 'w')
    f_public.write(str(public))

    f_public.close()
    private = (str(d)+'.'+str(n)).encode('ascii')
    private = base64.b64encode(private).decode()
    f_private = open('private_keys.txt', 'w')
    f_private.write(str(private))

    f_private.close()


