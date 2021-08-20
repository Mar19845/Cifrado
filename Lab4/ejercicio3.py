import math
import lcg as lcg
import lfsr as lfsr
import WichmanHill as Wichman_Hill
import matplotlib.pyplot as plt
import math
import numpy as np

#https://github.com/GINARTeam/NIST-statistical-test/blob/master/01_monobit_test.py
def test(input):
    n = len(input)  
    ones = input.count('1') #number of ones

    zeroes = input.count('0')    #number of zeros

    s = abs(ones - zeroes)  

    p = math.erfc(float(s)/(math.sqrt(float(n)) * math.sqrt(2.0))) #p-value

    success = ( p >= 0.01)  # success = true if p-value >= 0.01

    return success

def histogroma(lista):
    guds = 0
    fail = 0
    n = len(lista)
    for i in lista:
        x= test(i)
        if x == True:
            guds+=1
        if x == False:
            fail += 1
    print(guds,fail)
    plt.hist(x=[guds,fail])
    plt.show()
def init_histo(n):
    histo=[]
    for i in range(1000):
        histo.append(lcg.LCG(n=n))
        #histo.append(lfsr.lfsr(n,[4, 2, 5], 6))
        #histo.append(Wichman_Hill.Wichmann_Hill(n))

    histogroma(histo)

init_histo((255))
