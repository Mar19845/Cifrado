import random

def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False
                
        if isPrime:
            prime_list.append(n)

    p = random.choice(prime_list)
    q = random.choice(prime_list)
    
    modN(p, q)

def modN(p, q):

    N = p*q
    



