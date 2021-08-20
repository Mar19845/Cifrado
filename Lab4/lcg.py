import random
from random import seed
from random import randint
import numpy as np

kbits = 1
def LCG(m=2**31-1, a=1103515245, b=12345,n=10):
    x = np.random.choice(m)
    bits=""
    for i in range(0, n):
        x = (a*x + b) % m
        stb = ''.join(format(ord(i), '08b') for i in str(x))
        stb = stb[::-1]
        for i in range(0, kbits):
            bits+=stb[i]
    return bits
