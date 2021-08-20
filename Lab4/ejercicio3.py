import math
import lcg as lcg
import lfsr as lfsr
import WichmanHill as Wichman_Hill
import matplotlib.pyplot as plt
import math
import numpy as np
import tests as tst


def histogroma(lista):
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
        for i in resultado:
            print(i)
            break
    
    
def init_histo(n):
    results=[]
    for _ in range(1000):

        x=lcg.LCG(n=n)
        #x=lfsr.lfsr(n,[4, 2, 5], 6)
        #x=Wichman_Hill.Wichmann_Hill(n)
        results.append(tst.init_tests(x))
    #results=tst.init_tests(x)
    histogroma(results)
    
#387840
#400000
init_histo((5000))
