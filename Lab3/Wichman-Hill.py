import random
from random import randint

def Wichmann_Hill(val1, listlength):
    seed1 = randint(1, 30000)
    seed2 = randint(1, 30000)
    seed3 = randint(1, 30000)
    
    numlist = []
    for i in range(listlength):
       
        seed1 = 171 * seed1 % 30269
        seed2 = 172 * seed2 % 30307
        seed3 = 170 * seed3 % 30323

        numlist.append((float(seed1)/30269.0 + float(seed2)/30307.0 + float(seed3)/30323.0) % 1.0)
    #print(numlist[0:50])
    return numlist