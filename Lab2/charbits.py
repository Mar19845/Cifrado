import cleaner as cl
import binascii

def toBits(phrase):

    chainbit = []
    for i in phrase:
        w = cl.binaryCleaner(bin(ord(i)))
        print( i,"en binario:", w)
        chainbit.append(w)

    number = cl.listJoiner(chainbit, '')

    return number
    


def toChar(number):
    splitted = cl.chainBreaker(number, ' ', 8)
    element = splitted.split(' ')

    elements = list(map(int, element))
    print(type(elements[0]))
    #a = int(elements[0],2)
    #print(a)

