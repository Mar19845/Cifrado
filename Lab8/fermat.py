# Python3 program to find the smallest
# twin in given range
import random
from random import randint
# Iterative Function to calculate
# (a^n)%p in O(logy)
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

def isPrime(n, k):
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        #return True
        print("si es primo", n)
    else:
        for i in range(k):
            a = random.randint(2, n - 2)
            if power(a, n - 1, n) != 1:
                return False
    return True


def random_with_N_digits(n, k=5):
    cont = 0
    while True:
        range_start = 10**(n-1)
        range_end = (10**n)-1
        valor = randint(range_start, range_end)
        if isPrime(valor, k):
            return valor
        else:
            pass
        if cont == k:
            break 
    
random_with_N_digits(3)