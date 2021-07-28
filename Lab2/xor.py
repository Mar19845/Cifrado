import cleaner as cl
import matplotlib.pyplot as plt
import random
import numpy as np 

def xori(c1, c2):

    bits = []
    
    for i in c1:
        bits.append(i)
    bits = list(map(int, bits))

    bits1 = []
    for j in c2:
        bits1.append(j)
    bits1 = list(map(int, bits1))

    result = list(map(lambda x, y: x ^ y, bits, bits1))
    result = cl.listJoiner(result, '')
    
    #Texto plano
    fig, ax = plt.subplots()
    x= range(0,1)
    ax.plot(x)
    plt.xticks(range(0,2,1))
    n, bins, patches=plt.hist(bits)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Texo plano")
    plt.show()
    
    
    # texto bits
    fig, ax = plt.subplots()
    x= range(0,1)
    ax.plot(x)
    plt.xticks(range(0,2,1))
    n, bins, patches=plt.hist(bits1)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Texto en bits")
    plt.show()
    
    
    #conversion
    result1 = []
    fig, ax = plt.subplots()
    x= range(0,1)
    ax.plot(x)
    plt.xticks(range(0,2,1))
    result1 = list(map(lambda x, y: x ^ y, bits, bits1))
    n, bins, patches=plt.hist(result1 )
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Conversion")
    plt.show()

    return result


    
def rand_Bits(p):
    #codigo extraido de 
    #https://www.geeksforgeeks.org/python-program-to-generate-random-binary-string/
    # Variable to store the 
    # string
    key1 = ""
  
    # Loop to find the string
    # of desired length
    for i in range(p):
          
        # randint function to generate
        # 0, 1 randomly and converting 
        # the result into str
        temp = str(random.randint(0, 1))
  
        # Concatenatin the random 0, 1
        # to the final result
        key1 += temp
          
    return key1
   
def XOR(chain):
    chain2 = rand_Bits(len(chain))
    
    bits = []
    
    for i in chain:
        bits.append(i)
    bits = list(map(int, bits))

    bits1 = []
    for j in chain2:
        bits1.append(j)
    bits1 = list(map(int, bits1))

    result = list(map(lambda x, y: x ^ y, bits, bits1))
    result = cl.listJoiner(result, '')
    




