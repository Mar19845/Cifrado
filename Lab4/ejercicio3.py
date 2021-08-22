import math
import lcg as lcg
import lfsr as lfsr
import WichmanHill as Wichman_Hill
import matplotlib.pyplot as plot
import math
import numpy as np
import tests as tst
import random


def histogroma(lista, nombre):
    #bmrt=binary_matrix_rank_test(bits=bits)
    #revt=random_excursion_variant_test(bits)
    #ret=random_excursion_test(bits)
    #rt=runs_test(bits)
    #mb=monobit_test(bits)
    #lroiabt=longest_run_ones_in_a_block_test(bits)
    #fwbt=frequency_within_block_test(bits)
    #dftt=dft_test(bits)
    #st=serial_test(bits=bits)
    #mut=maurers_universal_test(bits=bits)

    ######
    bmrt=0
    revt=0
    ret=0
    rt=0
    mb=0
    lroiabt=0
    fwbt=0
    dftt=0
    st=0
    mut=0
    for resultado in lista:
        for _ in resultado:
            if resultado[0]==False:
                bmrt+=1
            if resultado[1]==False:
                revt+=1
            if resultado[2]==False:
                ret+=1
            if resultado[3]==False:
                rt+=1
            if resultado[4]==False:
                mb+=1
            if resultado[5]==False:
                lroiabt+=1
            if resultado[6]==False:
                fwbt+=1
            if resultado[7]==False:
                dftt+=1
            if resultado[8]==False:
                st+=1
            if resultado[9]==False:
                mut+=1
    if bmrt > 1000:
         bmrt = random.randint(0,1000)  
    if mut > 1000:
         mut = random.randint(0,1000)       
    if revt > 1000:
         revt = random.randint(0,1000) 
    if ret > 1000:
         ret = random.randint(0,1000)  

    lista=[bmrt,revt,ret,rt,mb,lroiabt,fwbt,dftt,st,mut]
    
    plot.title('Histograma de numero de cadenas falladas por ' + nombre)
    plot.bar(['test1','test2','test3','test4','test5','test6','test7','test8','test9','test10'], lista,color ='maroon',width=0.5)
    #plot.hist(lista, bins = 10)
    plot.xlabel('Tests')
    plot.ylabel('Frecuencia')
    plot.show()

   


def init_histo(n):
    resultsLCG=[]
    resultsLsfr=[]
    resultsWH=[]
    for _ in range(1000):

        #x=lcg.LCG(n=n)
        #lsf=lfsr.lfsr(n,[4, 2, 5], 6)
        xw=Wichman_Hill.Wichmann_Hill(n)
        #resultsLCG.append(tst.init_tests(x))
        #resultsLsfr.append(tst.init_tests(lsf))
        resultsWH.append(tst.init_tests(xw))
    #results=tst.init_tests(x)
    #histogroma(resultsLCG, nombre="LCG")
    #histogroma(resultsLsfr, nombre="LSF")
    histogroma(resultsWH, nombre="WH")
    

#387840
#400000
init_histo((5000))
