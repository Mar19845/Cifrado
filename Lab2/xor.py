import cleaner as cl
import matplotlib.pyplot as plt

def toBits(c1, c2):

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
    
    result1 = []
    result1 = list(map(lambda x, y: x ^ y, bits, bits1))
    n, bins, patches=plt.hist(bits1)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()

    return result

   


    
    
