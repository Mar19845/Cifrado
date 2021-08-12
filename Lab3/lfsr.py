import random as ran
    
def randomGen():
    number = ran.randint(0, 1)
    return number   

def lfsr(n, tap, loops):
    sd = ""
    bit = ""
    tap = sorted(tap, reverse = True)
    count = 0
    r = 0
    
    for num in range(n):
        x = randomGen()

        sd += str(x)
      
    print("No LFSR: " + sd)
    
    while (count != loops):
        x = int(sd[0])

        for num in tap[1:]:
            x = x ^ int(sd[num])
            
        sd = str(x) + sd
        count += 1
    
    print("LFSR: " + sd)
    

