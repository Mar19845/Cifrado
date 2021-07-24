import cleaner as cl
import binascii

def toBits(phrase):

    chainbit = []
    chainbitPass = []
    for i in phrase:
        k = bin(ord(i))
        w = cl.binaryCleaner(bin(ord(i)))
        print( i,"en binario:", w)
        chainbit.append(w)
        chainbitPass.append(k)
    number = cl.listJoiner(chainbit, '')

    return number, chainbitPass
    

def toChar(number):
    
    letters=[]
    for j in number:
        t = chr(int(j, 2))
        letters.append(t)
    phrase = cl.listJoiner(letters, '')

    return phrase
        #print(j)
    
    #a = int(elements[0],2)
    #print(a)

