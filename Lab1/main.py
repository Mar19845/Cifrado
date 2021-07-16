import numpy as np
import nltk
import re

alpha = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

texto = 'Hola mi nombre es Russel, soy de la tribu 57, desea que lo ayude a limpiar su portico'

def cleanTxt(tx):
    t = tx.upper()
    t = t.replace('Á','A')
    t = t.replace('É','E')
    t = t.replace('Í','I')
    t = t.replace('Ó','O')
    t = t.replace('Ú','U')
    remover = [' ','.',',','(',')','1','2','3','4','5','6','7','8','9','0']
    
    for w in remover:
        t = t.replace(w, '')
    return t

def ceasar(text,desp):
    text=cleanTxt(text)
    cipher = ''
    for i in range(len(text)):
        char = text[i]
        if (char.islower()):
            cipher += chr((ord(char) + desp - 97) % 26 + 97)  # 97 letra minuscula (a)
        else:
            cipher += chr((ord(char) + desp-65) % 26 + 65)  # Prima letra mayuscula (A)
    return cipher

def caesar_d(text,desp):
    text=cleanTxt(text)
    plain = ""
    for i in range(len(text)):
        char = text[i]
        if (char.islower()):
            plain += chr((ord(char) -97-desp) % 26 + 97)
        else:
            plain += chr((ord(char) -65-desp) % 26 + 65)
    return plain


t1 = ceasar(texto,4)
print(t1)

t2 = caesar_d(t1,4)
print(t2)