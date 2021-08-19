import random
from random import seed
from random import randint

def LCG( x,a, c, m):
    while True:
        x = (a * x + c) % m
        yield x


def init_lcg(n):
    x = random.randrange(0,n)
    #x=0
    cadena=''
    a, c, m = 45, 1, 2 ** 31
    lcg = LCG(x,a,c,m)
    for _ in range(n):
        
        bit = str(bin(next(lcg)))[2:]
        if len(bit)<2:
           cadena +=('0'+bit)
        else:
            cadena +=bit[-2:]
    if len(cadena)>n:
        
        return cadena[n:]
    else:
        return cadena
