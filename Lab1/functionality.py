import caesar as ca
import vigenere as vi
import afin as af
from afin import afinCypher
import numpy as np
import nltk
import re
import matplotlib.pyplot as plt

tprob = {'A': 0.1253, 'B': 0.0142, 'C': 0.0468, 'D': 0.0586, 'E': 0.1368, 'F': 0.0069, 'G': 0.0101, 'H': 0.007, 'I': 0.0625, 'J': 0.0044, 'K': 0.0002, 'L': 0.0497, 'M': 0.0315, 'N': 0.0671, 'Ñ': 0.0031, 'O': 0.0868, 'P': 0.0251, 'Q': 0.0088, 'R':0.0687, 'S':0.0798, 'T':0.0463, 'U': 0.0393, 'V': 0.009, 'W': 0.0001, 'X': 0.0022, 'Y': 0.009, 'Z': 0.0052}
alpha = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
afin_key = [7, 15]
afincypher = afinCypher(alpha, tprob)
#Tengo mis dudas sobre si dejar esta función aqui o si meterla en las funciones 
#encrypt para que limpie cada cosa, si tienen ideas son bienvenidas

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

    print("\nMENSAJE ENCRIPTADO EN AFIN: \n")

    mensaje=cleanTxt(mensaje)
    mCifrado = afincypher.encryptA(afin_key[0], afin_key[1], mensaje)
    print(mCifrado, "\n") 

    input("PRESIONA ENTER PARA DECRIPTAR\n")
    mDes=afincypher.decryptA(afin_key[0], afin_key[1], mCifrado)
    print(mDes, "\n")
    

def vigenereInit():
    
    text = input("Ingrese el mensaje que desea encriptar: ")
    clave = input("Ingrese la cantidad de letras trasladar: ")
    print("\nMENSAJE ENCRIPTADO EN AFIN: \n")
    text=cleanTxt(text)
    mCifrado = vi.encryptV(text, clave)
    print(mCifrado) 
    #encryptV()

    input("PRESIONA ENTER PARA DECRIPTAR\n")
    mDes= vi.decryptV(mCifrado, clave)
    print(mDes)
    print("")
    #decryptV()
    
def distribucion():
    mensaje = input("Ingrese un texto Cifrado o descrifrado: ")
    mensaje = cleanTxt(mensaje)
    dist = {
        'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'Ñ':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0
    }
    for i in mensaje:
        for j in alpha:
            if i==j:
                dist[i]=dist.get(i) + 1
    
    for i in dist:
        dist[i]= float(dist.get(i)/len(mensaje))

    return dist


def metica(dist):
    freq = {
        'A':0.11525,'B':0.02215,'C':0.04019,'D':0.05010,'E':0.12181,'F':0.00692,'G':0.01768,'H':0.00703,'I':0.06247,'J':0.00493,'K':0.00011,'L':0.04967,'M':0.03157,'N':0.06712,'Ñ':0.0311,'O':0.08683,'P':0.02510,'Q':0.00877,'R':0.06871,'S':0.07977,'T':0.04632,'U':0.02927,'V':0.01138,'W':0.00017,'X':0.00215,'Y':0.01008,'Z':0.00467
    }

    

    plt.figure(1)

    plt.subplot(211)
    plt.bar(range(len(freq)), list(freq.values()), align='center',color='red',label='Teorico')
    plt.xticks(range(len(freq)), list(freq.keys()))
    
    plt.ylabel('Frecuencias')
    plt.legend()

    plt.subplot(212)
    plt.bar(range(len(dist)), list(dist.values()), align='center',color='blue',label='Experimental')
    plt.xticks(range(len(dist)), list(dist.keys()))
    
    plt.ylabel('Frecuencias')
    plt.legend()

    plt.show()

def BrutoC():
    f = open("cipher1.txt", "r")
    cryptictext1 = f.read()
    cryptictext= cryptictext1.lower()
    for i in range(0,26):
        plain_text = ca.decryptC(cryptictext, i)
        if i == 19:
            print("La clave resultante es {}, el mensaje desencriptado es: \n\n{}".format(i, plain_text))
            print("")

def BrutoA():

    message, llave = afincypher.fuerzabrutaAfin("QHNHVPEKHVHVRRMIRYERARMTECJZRVRYEQCBHIRPPCLBRJRQHRPBXERPIBCJIRPJHZCBJHQQHHEPBPHVRKEHIRNHQHRQHACBJTERIPHYBEJQBIRVRIPRMZCRJIHMVCRLNCQVBMCMVRAHZEJHMXEIJCUATERMRPACPHJXHPHZBJICJEHPZBJRQXQHJJHZCBJHQVRAHZEJHZCBJZBJIPHRQZBPBJHACPEMBPCKCJHQNRJIRRQHACBJCDHHHIRPPCLHPRJKEHIRNHQHRQNCRPZBQRMHQHMACRCJICEJHGBPHMXRPBQERKBMRCJÑBPNBTERRQAERQBMRGHDCHPRIPHMHVBOXBPRMBQQRKBHQXHCMHRMBVRQHMZEHIPBGBPHMVRRMIRYERARMRQNCJCMIRPCBVRMHQEVCJÑBPNBTERRQHACBJIPHYBIPRMZCRJIHMVCRLNCQVBMCMVRQDCBQBKCZBPEMBVRQHMZEHQRMMRMRJIHNCQMBJMRKEJVHMVBMCMOVBMZCRJIBMZCJZERJIHNCQXPCNRPHMVBMCMHVCÑRPRJZCHVRBIPHMAHZEJHMRQDCBQBKCZBVRPEMCHICRJRVBMZBNXBJRJIRMEJBTERMREICQCLHXHPHQHXPCNRPHVBMCMOBIPBXHPHRQPRÑERPLBORMIRZHPKHNRJIBVRMRMRJIHNCQMCKJCÑCZHPCHRQXPCNRPBTERPRZCDRRQXHCMVRMRKEJVHMVBMCMZBJRMIHMVBMCMMRZBJICJEHPHZBJRQXQHJJHZCBJHQVRAHZEJHZCBJOMRCJCZCHPHZBJQHHVNCJCMIPHZCBJVRQHMMRKEJVHMVBMCMZEHJVBQHMXPCNRPHMXRPMBJHMCJNEJCLHVHMZBJMXEIJCUAZENXQHJMEMJBARJIHVCHMVRGHDRPPRZCDCVBQHXPCNRPHVBMCMZCIHQHCJÑBPNHZCBJVRQNCJCMIRPCBVRMHQEV")
    print('La llave de encriptacion es: ', llave,'y el mensaje es:\n\n', message, '\n')