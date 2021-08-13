import random
from random import randint

def Wichmann_Hill(listlength):
    seed1 = randint(1, 30000)
    seed2 = randint(1, 30000)
    seed3 = randint(1, 30000)
    
    k = ''
    for i in range(listlength):
       
        seed1 = 171 * seed1 % 30269
        seed2 = 172 * seed2 % 30307
        seed3 = 170 * seed3 % 30323

        numlist = ((float(seed1)/30269 + float(seed2)/30307 + float(seed3)/30323) % 1)
        k += str(round(numlist))
        
    return(k)