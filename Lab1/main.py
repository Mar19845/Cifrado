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

t1 = cleanTxt(texto1)
print(t1)