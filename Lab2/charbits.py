import cleaner as cl
def toBits(phrase):

    chainbit = []
    for i in phrase:
        w = cl.binaryCleaner(bin(ord(i)))
        print( i,"en binario:", w)
        chainbit.append(w)

    number = cl.listJoiner(chainbit, '')

    return number
    


def toChar(bits):
    for i in bits:
        w = ord(bin(i))
        print("Codigo binario de", i,":", w)
    return w