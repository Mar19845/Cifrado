import math
import lcg as lcg
import lfsr as lfsr
import WichmanHill as Wichman_Hill
import matplotlib.pyplot as plt

#https://github.com/GINARTeam/NIST-statistical-test/blob/master/01_monobit_test.py
#monobit_test
def test(input, n):
        
    ones = input.count('1') #number of ones

    zeroes = input.count('0')    #number of zeros

    s = abs(ones - zeroes)  

    p = math.erfc(float(s)/(math.sqrt(float(n)) * math.sqrt(2.0))) #p-value

    success = ( p >= 0.01)  # success = true if p-value >= 0.01

    return [zeroes, ones, s, p, success]

def histogroma(lista):
    print('ads')
def init_histo(n):
    histo=[]
    for i in range(1000):
        histo.append(lcg.init_lcg(n))
        #histo.append(lfsr.lfsr(n,[4, 2, 5], 6))
        #histo.append(Wichman_Hill.Wichmann_Hill(n))

    histogroma(histo)

init_histo(10)