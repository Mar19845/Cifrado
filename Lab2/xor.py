import cleaner as cl

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
    
    return result

    
