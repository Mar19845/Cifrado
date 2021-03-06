import random
from random import randint
import fermat as fmt

def Diffie_Hellman(n=2):
    p = fmt.random_with_N_digits(n)
    q= randint(2,p-1)
    #private keys
    A_private_key = randint(2,p-1)
    B_private_key = randint(1,p-1)
    A_public_key = pow(p,A_private_key,q) #p**A_private_key% q
    B_public_key = pow(p,B_private_key,q) #p**B_private_key% q
    #calc a and b same keys
    A = pow(B_public_key,A_private_key,q)#B_public_key**A_private_key % q
    B = pow(A_public_key,B_private_key,q)#A_public_key**B_private_key % q
    return A, B
