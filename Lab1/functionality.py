from caesar import *
from vigenere import *
from afin import *

import numpy as np
import nltk
import re

alpha = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

#Tengo mis dudas sobre si dejar esta función aqui o si meterla en las funciones 
#encrypt para que limpie cada cosa, si tienen ideas son bienvenidas

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

#Funciones para llamar al metodo de encriptacion que querramos, la idea es que por cada vez que el usuario elija
#encriptar o decriptar borre lo que esta en el .txt y lo reescriba para asegurarnos que funciona
#tambien hay que hacer lo de las distribuciuones de frecuencias y probabilidades

def caesarInit():

    f = open("cipher1.txt", "r")
    print("MENSAJE ENCRIPTADO EN CAESAR: \n")
    caesar = f.read()
    print(caesar, "\n")

    input("PRESIONA ENTER PARA DECRIPTAR\n") 
    decryptC()

    input("PRESIONA ENTER PARA ENCRIPTAR DE NUEVO\n")
    encryptV()
    
    
def afinInit():

    f = open("cipher2.txt", "r")
    print("MENSAJE ENCRIPTADO EN AFÍN \n")
    afin = f.read()
    print(afin, "\n")

    input("PRESIONA ENTER PARA DECRIPTAR\n")
    decryptA()

    input("PRESIONA ENTER PARA ENCRIPTAR DE NUEVO\n")
    encryptA()
    

def vigenereInit():
    
    f = open("cipher3.txt", "r")
    print("MENSAJE ENCRIPTADO EN VIGENERE: \n")
    vig = f.read()
    print(vig, "\n")

    input("PRESIONA ENTER PARA DECRIPTAR\n")
    decryptV()

    input("PRESIONA ENTER PARA ENCRIPTAR DE NUEVO\n")
    encryptV()
    