import caesar as ca
import vigenere as vi
import afin as af

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

    mensaje = input("Ingrese el mensaje que desea encriptar: ")
    paso = int(input("Ingrese la cantidad de letras trasladar: "))

    print("\nMENSAJE ENCRIPTADO EN CAESAR: \n")

    mensaje=cleanTxt(mensaje)
    mCifrado = ca.encryptC(mensaje, paso)
    print(mCifrado, "\n") 

    input("PRESIONA ENTER PARA DECRIPTAR\n")
    mDes=ca.decryptC(mCifrado, paso)
    print(mDes, "\n")
    
    
def afinInit():

    mensaje = input("Ingrese el mensaje que desea encriptar: ")
    paso = int(input("Ingrese la cantidad de letras trasladar: "))

    print("\nMENSAJE ENCRIPTADO EN AFIN: \n")

    mensaje=cleanTxt(mensaje)
    mCifrado = af.encryptA(mensaje, paso)
    print(mCifrado, "\n") 

    input("PRESIONA ENTER PARA DECRIPTAR\n")
    mDes=af.decryptA(mCifrado, paso)
    print(mDes, "\n")
    

def vigenereInit():
    
    text = input("Ingrese el mensaje que desea encriptar: ")
    clave = input("Ingrese la cantidad de letras trasladar: ")
    
    input("PRESIONA ENTER PARA ENCRIPTAR DE NUEVO\n")  
    text=cleanTxt(text)
    mCifrado = vi.encryptV(text, clave)
    #encryptV()

    input("PRESIONA ENTER PARA DECRIPTAR\n")
    print(mCifrado) 
    mDes= vi.decryptV(mCifrado, clave)
    print(mDes)
    print("")
    #decryptV()
    
