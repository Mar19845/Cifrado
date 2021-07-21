from nltk import *


alfab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
percent = [('a', 0.12027), ('b', 0.02215), ('c', 0.04019), ('d', 0.05010), ('e', 0.12614),
                ('f', 0.00692), ('g', 0.01768), ('h', 0.00703), ('i', 0.06972), ('j', 0.00493),
                ('k', 0.00011), ('l', 0.04967), ('m', 0.03157), ('n', 0.06712), ('ñ', 0.00311),
                ('o', 0.0951), ('p', 0.02510), ('q', 0.00877), ('r', 0.06871), ('s', 0.07977),
                ('t', 0.04632), ('u', 0.03107), ('v', 0.01138), ('w', 0.00017), ('x', 0.00215),
                ('y', 0.01008), ('z', 0.00467)]

def encryptA(mensaje, wa, b):
    words = list(mensaje)
    #print(words)
    for i in words:
        for j in alfab:
            if (i == j):
                words[words.index(i)] = alfab.index(j)
    #print(words)
    words = [(wa * element + b) % 27 for element in words]
    #print(words)
    for n, i in enumerate(words):
        words[n] = alfab[i]
    #print(words)
    cifrado = ''
    cifrado = cifrado.join(words)
    return cifrado 

def InversoAritmetico(a):
    AInverse = 1
    while (AInverse * a) % 27 != 1:
        AInverse += 1
    return AInverse

def decryptA(cifrado, a, b):
    words2 = list(cifrado)
    #print(words2)
    for i in words2:
        for j in alfab:
            if (i == j):
                words2[words2.index(i)] = alfab.index(j)
    #print(words2)
    
    words2 = [(InversoAritmetico(wa) * (element - b)) % 27 for element in words2]
    
    #print(words2)
    for n, i in enumerate(words2):
        words2[n] = alfab[i]
    descifrado = ''
    descifrado = descifrado.join(words2)
    return descifrado

def Distribucion():
    fraseDist = FreqDist(encryptA()).most_common(27)
    total = 0
    porcentajes = []
    for i in fraseDist:
        total = total + fraseDist[fraseDist.index(i)][1]
    for i in fraseDist:
        porcentajes.append(fraseDist[fraseDist.index(i)][1]/total)
    return porcentajes