def cleanTxt(tx):
    t = tx.upper()
    t = t.replace('Á','A')
    t = t.replace('É','E')
    t = t.replace('Í','I')
    t = t.replace('Ó','O')
    t = t.replace('Ú','U')
    t = t.replace('Ü','U')
    remover = [' ','.',',','(',')','1','2','3','4','5','6','7','8','9','0']
    
    for w in remover:
        t = t.replace(w, '')
    return t

def binaryCleaner(binary):

    t = binary

    remover = [' ','b','B']

    for l in remover:
        t = t.replace(l,'')

    return t

def listJoiner(lista, caracter):
    if isinstance(lista, list):
        return caracter.join(map(str, lista))

    raise TypeError("El parámetro lista debe ser una lista")

def chainBreaker(number, splitter, step):
    a = ''
    count = 0
    for i in number[::-1]:
        if count == step:    
            a += splitter
            count = 0
        count += 1
        a += i
    return("".join(reversed(a)))
    