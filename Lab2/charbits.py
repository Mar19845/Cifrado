import cleaner as cl
def toBits(phrase):

    for i in phrase:
        w = cl.binaryCleaner(bin(ord(i)))
        print("Codigo ascii de", i,":", w)
    return w


def toChar(bits):
    for i in bits:
        w = ord(bin(i))
        print("Codigo binario de", i,":", w)
    return w