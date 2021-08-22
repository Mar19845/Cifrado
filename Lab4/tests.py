from __future__ import print_function

import math
from gamma_functions import *
import numpy
import sys
from fractions import Fraction
import cmath
import random
#import GF2Matrix
#import gf2matrix

#Cumulative Test 1

def normcdf(n):
    return 0.5 * math.erfc(-n * math.sqrt(0.5))

def p_value(n,z):
    sum_a = 0.0
    startk = int(math.floor((((float(-n)/z)+1.0)/4.0)))
    endk   = int(math.floor((((float(n)/z)-1.0)/4.0)))
    for k in range(startk,endk+1):
        c = (((4.0*k)+1.0)*z)/math.sqrt(n)
        #d = scipy.stats.norm.cdf(c)
        d = normcdf(c)
        c = (((4.0*k)-1.0)*z)/math.sqrt(n)
        #e = scipy.stats.norm.cdf(c)
        e = normcdf(c)
        sum_a = sum_a + d - e

    sum_b = 0.0
    startk = int(math.floor((((float(-n)/z)-3.0)/4.0)))
    endk   = int(math.floor((((float(n)/z)-1.0)/4.0)))
    for k in range(startk,endk+1):
        c = (((4.0*k)+3.0)*z)/math.sqrt(n)
        #d = scipy.stats.norm.cdf(c)
        d = normcdf(c)
        c = (((4.0*k)+1.0)*z)/math.sqrt(n)
        #e = scipy.stats.norm.cdf(c)
        e = normcdf(c)
        sum_b = sum_b + d - e 

    p = 1.0 - sum_a + sum_b
    return p
    
def cumulative_sums_test(bits):
    n = len(bits)
    # Step 1
    x = list()             # Convert to +1,-1
    for bit in bits:
        #if bit == 0:
        x.append((bit*2)-1)
        
    # Steps 2 and 3 Combined
    # Compute the partial sum and records the largest excursion.
    pos = 0
    forward_max = 0
    for e in x:
        pos = pos+e
        if abs(pos) > forward_max:
            forward_max = abs(pos)
    pos = 0
    backward_max = 0
    for e in reversed(x):
        pos = pos+e
        if abs(pos) > backward_max:
            backward_max = abs(pos)
     
    # Step 4
    p_forward  = p_value(n, forward_max)
    p_backward = p_value(n,backward_max)
    
#DFT TESTS 2

def dft_test(bits):
    n = len(bits)
    if (n % 2) == 1:        # Make it an even number
        bits = bits[:-1]

    ts = list()             # Convert to +1,-1
    for bit in bits:
        ts.append((bit*2)-1)

    ts_np = numpy.array(ts)
    fs = numpy.fft.fft(ts_np)  # Compute DFT
   
    if sys.version_info > (3,0):
        mags = abs(fs)[:n//2] # Compute magnitudes of first half of sequence
    else:
        mags = abs(fs)[:n/2] # Compute magnitudes of first half of sequence
    
    T = math.sqrt(math.log(1.0/0.05)*n) # Compute upper threshold
    N0 = 0.95*n/2.0
    #print("  N0 = %f" % N0)

    N1 = 0.0   # Count the peaks above the upper theshold
    for mag in mags:
        if mag < T:
            N1 += 1.0
    #print("  N1 = %f" % N1)
    d = (N1 - N0)/math.sqrt((n*0.95*0.05)/4) # Compute the P value
    p = math.erfc(abs(d)/math.sqrt(2))

    success = (p >= 0.01)
    return success

#frequency_within_block_test 3

#ones_table = [bin(i)[2:].count('1') for i in range(256)]
def count_ones_zeroes(bits):
    ones = 0
    zeroes = 0
    for bit in bits:
        if (bit == 1):
            ones += 1
        else:
            zeroes += 1
    return (zeroes,ones)

def frequency_within_block_test(bits):
    # Compute number of blocks M = block size. N=num of blocks
    # N = floor(n/M)
    # miniumum block size 20 bits, most blocks 100
    n = len(bits)
    M = 20
    N = int(math.floor(n/M))
    if N > 99:
        N=99
        M = int(math.floor(n/N))
    
    if len(bits) < 100:
        #print("Too little data for test. Supply at least 100 bits")
        return False
    
    #print("  n = %d" % len(bits))
    #print("  N = %d" % N)
    #print("  M = %d" % M)
    
    num_of_blocks = N
    block_size = M #int(math.floor(len(bits)/num_of_blocks))
    #n = int(block_size * num_of_blocks)
    
    proportions = list()
    for i in range(num_of_blocks):
        block = bits[i*(block_size):((i+1)*(block_size))]
        zeroes,ones = count_ones_zeroes(block)
        proportions.append(Fraction(ones,block_size))

    chisq = 0.0
    for prop in proportions:
        chisq += 4.0*block_size*((prop - Fraction(1,2))**2)
    
    p = gammaincc((num_of_blocks/2.0),float(chisq)/2.0)
    success = (p >= 0.01)
    return success


#longest_run_ones_in_a_block_test 4

def probs(K,M,i):
    M8 =      [0.2148, 0.3672, 0.2305, 0.1875]
    M128 =    [0.1174, 0.2430, 0.2493, 0.1752, 0.1027, 0.1124]
    M512 =    [0.1170, 0.2460, 0.2523, 0.1755, 0.1027, 0.1124]
    M1000 =   [0.1307, 0.2437, 0.2452, 0.1714, 0.1002, 0.1088]
    M10000 =  [0.0882, 0.2092, 0.2483, 0.1933, 0.1208, 0.0675, 0.0727]
    if (M == 8):        return M8[i]
    elif (M == 128):    return M128[i]
    elif (M == 512):    return M512[i]
    elif (M == 1000):   return M1000[i]
    else:               return M10000[i]

def longest_run_ones_in_a_block_test(bits):
    n = len(bits)

    if n < 128:
        return False
    elif n<6272:
        M = 8
    elif n<750000:
        M = 128
    else:
        M = 10000
            
    # compute new values for K & N
    if M==8:
        K=3
        N=16
    elif M==128:
        K=5
        N=49
    else:
        K=6
        N=75
        
    # Table of frequencies
    v = [0,0,0,0,0,0,0]

    for i in range(N): # over each block
        #find longest run
        block = bits[i*M:((i+1)*M)] # Block i
        
        run = 0
        longest = 0
        for j in range(M): # Count the bits.
            if block[j] == 1:
                run += 1
                if run > longest:
                    longest = run
            else:
                run = 0

        if M == 8:
            if longest <= 1:    v[0] += 1
            elif longest == 2:  v[1] += 1
            elif longest == 3:  v[2] += 1
            else:               v[3] += 1
        elif M == 128:
            if longest <= 4:    v[0] += 1
            elif longest == 5:  v[1] += 1
            elif longest == 6:  v[2] += 1
            elif longest == 7:  v[3] += 1
            elif longest == 8:  v[4] += 1
            else:               v[5] += 1
        else:
            if longest <= 10:   v[0] += 1
            elif longest == 11: v[1] += 1
            elif longest == 12: v[2] += 1
            elif longest == 13: v[3] += 1
            elif longest == 14: v[4] += 1
            elif longest == 15: v[5] += 1
            else:               v[6] += 1
    
    # Compute Chi-Sq
    chi_sq = 0.0
    for i in range(K+1):
        p_i = probs(K,M,i)
        upper = (v[i] - N*p_i)**2
        lower = N*p_i
        chi_sq += upper/lower
    #print("  n = "+str(n))
    #print("  K = "+str(K))
    #print("  M = "+str(M))
    #print("  N = "+str(N))
    #print("  chi_sq = "+str(chi_sq))
    p = gammaincc(K/2.0, chi_sq/2.0)
    
    success = (p >= 0.01)
    return success

    
#MONOBITS TEST 5

def count_ones_zeroes(bits):
    ones = 0
    zeroes = 0
    for bit in bits:
        if (bit == 1):
            ones += 1
        else:
            zeroes += 1
    return (zeroes,ones)

def monobit_test(bits):
    n = len(bits)
    
    zeroes,ones = count_ones_zeroes(bits)
    s = abs(ones-zeroes)
    #print("  Ones count   = %d" % ones)
    #print("  Zeroes count = %d" % zeroes)
    
    p = math.erfc(float(s)/(math.sqrt(float(n)) * math.sqrt(2.0)))
    
    success = (p >= 0.01)
    return success

#RUNS TESTS 6

def count_ones_zeroes(bits):
    ones = 0
    zeroes = 0
    for bit in bits:
        if (bit == 1):
            ones += 1
        else:
            zeroes += 1
    return (zeroes,ones)

def runs_test(bits):
    n = len(bits)
    zeroes,ones = count_ones_zeroes(bits)

    prop = float(ones)/float(n)
    #print("  prop ",prop)

    tau = 2.0/math.sqrt(n)
    #print("  tau ",tau)

    if abs(prop-0.5) > tau:
        return False,

    vobs = 1.0
    for i in range(n-1):
        if bits[i] != bits[i+1]:
            vobs += 1.0

    #print("  vobs ",vobs)
      
    p = math.erfc(abs(vobs - (2.0*n*prop*(1.0-prop)))/(2.0*math.sqrt(2.0*n)*prop*(1-prop) ))
    success = (p >= 0.01)
    return success

# RANDOM EXCURSION TEST 7
def random_excursion_test(bits):
    n = len(bits)

    x = list()             # Convert to +1,-1
    for bit in bits:
        #if bit == 0:
        x.append((bit*2)-1)

    ##print "x=",x
    # Build the partial sums
    pos = 0
    s = list()
    for e in x:
        pos = pos+e
        s.append(pos)    
    sprime = [0]+s+[0] # Add 0 on each end
    
    ##print "sprime=",sprime
    # Build the list of cycles
    pos = 1
    cycles = list()
    while (pos < len(sprime)):
        cycle = list()
        cycle.append(0)
        while sprime[pos]!=0:
            cycle.append(sprime[pos])
            pos += 1
        cycle.append(0)
        cycles.append(cycle)
        pos = pos + 1
    
    J = len(cycles)
    #print("J="+str(J))    
    
    vxk = [['a','b','c','d','e','f'] for y in [-4,-3,-2,-1,1,2,3,4] ]

    # Count Occurances  
    for k in range(6):
        for index in range(8):
            mapping = [-4,-3,-2,-1,1,2,3,4]
            x = mapping[index]
            cyclecount = 0
            #count how many cycles in which x occurs k times
            for cycle in cycles:
                oc = 0
                #Count how many times x occurs in the current cycle
                for pos in cycle:
                    if (pos == x):
                        oc += 1
                # If x occurs k times, increment the cycle count
                if (k < 5):
                    if oc == k:
                        cyclecount += 1
                else:
                    if k == 5:
                        if oc >=5:
                            cyclecount += 1
            vxk[index][k] = cyclecount
    
    # Table for reference random probabilities
    pixk=[[0.5     ,0.25   ,0.125  ,0.0625  ,0.0312 ,0.0312],
          [0.75    ,0.0625 ,0.0469 ,0.0352  ,0.0264 ,0.0791],
          [0.8333  ,0.0278 ,0.0231 ,0.0193  ,0.0161 ,0.0804],
          [0.875   ,0.0156 ,0.0137 ,0.012   ,0.0105 ,0.0733],
          [0.9     ,0.01   ,0.009  ,0.0081  ,0.0073 ,0.0656],
          [0.9167  ,0.0069 ,0.0064 ,0.0058  ,0.0053 ,0.0588],
          [0.9286  ,0.0051 ,0.0047 ,0.0044  ,0.0041 ,0.0531]]
    
    success = True
    plist = list()
    for index in range(8):
        mapping = [-4,-3,-2,-1,1,2,3,4]
        x = mapping[index]
        chisq = 0.0
        for k in range(6):
            top = float(vxk[index][k]) - (float(J) * (pixk[abs(x)-1][k]))
            top = top*top
            bottom = J * pixk[abs(x)-1][k]
            chisq += top/bottom
        p = gammaincc(5.0/2.0,chisq/2.0)
        plist.append(p)
        if p < 0.01:
            err = " Not Random"
            success = False
        else:
            err = ""
        #print("x = %1.0f\tchisq = %f\tp = %f %s"  % (x,chisq,p,err))
    #if (J < 500):
        #print("J too small (J < 500) for result to be reliable")
    #elif success:
        #print("PASS")
    #else:    
        #print("FAIL: Data not random")
    return success



# RANDOM EXCURSION VARIANT TEST 8
def random_excursion_variant_test(bits):
    n = len(bits)

    x = list()             # Convert to +1,-1
    for bit in bits:
        x.append((bit * 2)-1)

    # Build the partial sums
    pos = 0
    s = list()
    for e in x:
        pos = pos+e
        s.append(pos)    
    sprime = [0]+s+[0] # Add 0 on each end

    # Count the number of cycles J
    J = 0
    for value in sprime[1:]:
        if value == 0:
            J += 1
    #print("J=",J)
    # Build the counts of offsets
    count = [0 for x in range(-9,10)]
    for value in sprime:
        if (abs(value) < 10):
            count[value] += 1

    # Compute P values
    success = True
    plist = list()
    for x in range(-9,10):
        if x != 0:
            top = abs(count[x]-J)
            bottom = math.sqrt(2.0 * J *((4.0*abs(x))-2.0))
            p = math.erfc(top/bottom)
            plist.append(p)
            if p < 0.01:
                err = " Not Random"
                success = False
            else:
                err = ""
            #print("x = %1.0f\t count=%d\tp = %f %s"  % (x,count[x],p,err))
            
    #if (J < 500):
        #print("J too small (J=%d < 500) for result to be reliable" % J)
    #elif success:
        #print("PASS")
   # else:    
        #print("FAIL: Data not random")
    return success
    
    #Binary Matrix test
def binary_matrix_rank_test(bits,M=32,Q=32):
    n = len(bits)
    N = int(math.floor(n/(M*Q))) #Number of blocks
    #print("  Number of blocks %d" % N)
    #print("  Data bits used: %d" % (N*M*Q))
    #print("  Data bits discarded: %d" % (n-(N*M*Q))) 
    
    if N < 38:
        #print("  Number of blocks must be greater than 37")
        p = 0.0
        return False
        
    # Compute the reference probabilities for FM, FMM and remainder 
    r = M
    product = 1.0
    for i in range(r):
        upper1 = (1.0 - (2.0**(i-Q)))
        upper2 = (1.0 - (2.0**(i-M)))
        lower = 1-(2.0**(i-r))
        product = product * ((upper1*upper2)/lower)
    FR_prob = product * (2.0**((r*(Q+M-r)) - (M*Q)))
    
    r = M-1
    product = 1.0
    for i in range(r):
        upper1 = (1.0 - (2.0**(i-Q)))
        upper2 = (1.0 - (2.0**(i-M)))
        lower = 1-(2.0**(i-r))
        product = product * ((upper1*upper2)/lower)
    FRM1_prob = product * (2.0**((r*(Q+M-r)) - (M*Q)))
    
    LR_prob = 1.0 - (FR_prob + FRM1_prob)
    
    FM = 0      # Number of full rank matrices
    FMM = 0     # Number of rank -1 matrices
    remainder = 0
    for blknum in range(N):
        block = bits[blknum*(M*Q):(blknum+1)*(M*Q)]
        # Put in a matrix
        matrix = GF2Matrix.matrix_from_bits(M,Q,block,blknum) 
        #matrix = gf2matrix.matrix_from_bits(M,Q,block,blknum) 
        # Compute rank
        rank = GF2Matrix.rank(M,Q,matrix,blknum)
        #rank = gf2matrix.rank(M,Q,matrix,blknum)
        if rank == M: # count the result
            FM += 1
        elif rank == M-1:
            FMM += 1  
        else:
            remainder += 1

    chisq =  (((FM-(FR_prob*N))**2)/(FR_prob*N))
    chisq += (((FMM-(FRM1_prob*N))**2)/(FRM1_prob*N))
    chisq += (((remainder-(LR_prob*N))**2)/(LR_prob*N))
    p = math.e **(-chisq/2.0)
    success = (p >= 0.01)
    
    #print("  Full Rank Count  = ",FM)
    #print("  Full Rank -1 Count = ",FMM)
    #print("  Remainder Count = ",remainder) 
    #print("  Chi-Square = ",chisq)

    return success
#serial test
def int2patt(n,m):
    pattern = list()
    for i in range(m):
        pattern.append((n >> i) & 1)
    return pattern
    
def countpattern(patt,bits,n):
    thecount = 0
    for i in range(n):
        match = True
        for j in range(len(patt)):
            if patt[j] != bits[i+j]:
                match = False
        if match:
            thecount += 1
    return thecount

def psi_sq_mv1(m, n, padded_bits):
    counts = [0 for i in range(2**m)] 
    for i in range(2**m):
        pattern = int2patt(i,m)
        count = countpattern(pattern,padded_bits,n)
        counts.append(count)
        
    psi_sq_m = 0.0
    for count in counts: 
        psi_sq_m += (count**2)
    psi_sq_m = psi_sq_m * (2**m)/n 
    psi_sq_m -= n
    return psi_sq_m            
         
def serial_test(bits,patternlen=None):
    n = len(bits)
    if patternlen != None:
        m = patternlen  
    else:  
        m = int(math.floor(math.log(n,2)))-2
    
        if m < 4:
            #print("Error. Not enough data for m to be 4")
            return False
        m = 4
    
    # Step 1
    padded_bits=bits+bits[0:m-1]
    
    # Step 2
    psi_sq_m   = psi_sq_mv1(m, n, padded_bits)
    psi_sq_mm1 = psi_sq_mv1(m-1, n, padded_bits)
    psi_sq_mm2 = psi_sq_mv1(m-2, n, padded_bits)    
    
    delta1 = psi_sq_m - psi_sq_mm1
    delta2 = psi_sq_m - (2*psi_sq_mm1) + psi_sq_mm2
    
    P1 = gammaincc(2**(m-2),delta1/2.0)
    P2 = gammaincc(2**(m-3),delta2/2.0)
        
    #print("  psi_sq_m   = ",psi_sq_m)
    #print("  psi_sq_mm1 = ",psi_sq_mm1)
    #print("  psi_sq_mm2 = ",psi_sq_mm2)
    #print("  delta1     = ",delta1)
    #print("  delta2     = ",delta2)  
    #print("  P1         = ",P1)
    #print("  P2         = ",P2)
     
    success = (P1 >= 0.01) and (P2 >= 0.01)
    return success


#[0,1,1,0,1,1,0,1,0,1]
def pattern2int(pattern):
    l = len(pattern)
    n = 0
    for bit in (pattern):
        n = (n << 1) + bit
    return n          
         
def maurers_universal_test(bits,patternlen=None, initblocks=None):
    n = len(bits)

    # Step 1. Choose the block size
    if patternlen != None:
        L = patternlen  
    else: 
        ns = [904960,2068480,4654080,10342400,
              22753280,49643520,107560960,
              231669760,496435200,1059061760]
        L = 6
        if n < 387840:
            #print("Error. Need at least 387840 bits. Got %d." % n)
            #exit()
            return False
        for threshold in ns:
            if n >= threshold:
                L += 1 

    # Step 2 Split the data into Q and K blocks
    nblocks = int(math.floor(n/L))
    if initblocks != None:
        Q = initblocks
    else:
        Q = 10*(2**L)
    K = nblocks - Q
    
    # Step 3 Construct Table
    nsymbols = (2**L)
    T=[0 for x in range(nsymbols)] # zero out the table
    for i in range(Q):             # Mark final position of
        pattern = bits[i*L:(i+1)*L] # each pattern
        idx = pattern2int(pattern)
        T[idx]=i+1      # +1 to number indexes 1..(2**L)+1
                        # instead of 0..2**L
    # Step 4 Iterate
    sum = 0.0
    for i in range(Q,nblocks):
        pattern = bits[i*L:(i+1)*L]
        j = pattern2int(pattern)
        dist = i+1-T[j]
        T[j] = i+1
        sum = sum + math.log(dist,2)
    #print("  sum =", sum)
    
    # Step 5 Compute the test statistic
    fn = sum/K
    #print("  fn =",fn)
       
    # Step 6 Compute the P Value
    # Tables from https://static.aminer.org/pdf/PDF/000/120/333/
    # a_universal_statistical_test_for_random_bit_generators.pdf
    ev_table =  [0,0.73264948,1.5374383,2.40160681,3.31122472,
                 4.25342659,5.2177052,6.1962507,7.1836656,
                 8.1764248,9.1723243,10.170032,11.168765,
                 12.168070,13.167693,14.167488,15.167379]
    var_table = [0,0.690,1.338,1.901,2.358,2.705,2.954,3.125,
                 3.238,3.311,3.356,3.384,3.401,3.410,3.416,
                 3.419,3.421]
                 
    # sigma = math.sqrt(var_table[L])
    mag = abs((fn - ev_table[L]) / ((0.7 - 0.8 / L + (4 + 32 / L) * (pow(K, -3 / L)) / 15) * (math.sqrt(var_table[L] / K)) * math.sqrt(2)))
    P = math.erfc(mag)

    success = (P >= 0.01)
    return success



def convert_bit_string(cadena):
    bits = []
    for i in cadena:
        bits.append(int(i))
    return bits
    
def init_tests(cadena):
    bits = convert_bit_string(cadena)
    #tests
    bmrt=binary_matrix_rank_test(bits=bits)
    revt=random_excursion_variant_test(bits)
    ret=random_excursion_test(bits)
    rt=runs_test(bits)
    mb=monobit_test(bits)
    lroiabt=longest_run_ones_in_a_block_test(bits)
    fwbt=frequency_within_block_test(bits)
    dftt=dft_test(bits)
    st=serial_test(bits=bits)
    mut=maurers_universal_test(bits=bits)

    results_test=[bmrt,revt,ret,rt,mb,lroiabt,fwbt,dftt,st,mut]

    return results_test
    
    
