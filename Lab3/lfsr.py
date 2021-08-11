from random import *
    
def LFSR(n, tap, loops):
    sd = ""
    tap = sorted(tap, reverse = True)
    cont = 0
    r = 0
    
    for i in range(n):
        x = randomNumber()

        sd += str(x)
      
    print("No LFSR: " + sd)
    
    while (cont != loops):
        x = int(sd[0])
        for i in tap[1:]:
            x = x ^ int(sd[i])
            
        sd = str(x) + sd
        cont += 1
    
    print("LFSR: " + sd)
    
def randomNumber():
    num = randint(0, 1)
    return num   

LFSR(8, [3, 1, 5], 3)