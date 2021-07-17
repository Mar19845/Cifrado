import functionality as func
import caesar as ca

def get_desp(char):
    return (ord(char.upper())-65)

def decryptV(text,clave):
    result = ""
    for i in range(0,len(text)): #Para todo el texto
        desp = get_desp(clave[i % len(clave)]) #Obtenemos el desplazamiento asociado a la clave
        result +=(ca.decryptC(text[i],desp)) #desciframos la letra con caesar para el desplazamiento dado
    print("Decifrado\n")
    return result



def encryptV(text,clave):
    result = ""
    for i in range(0,len(text)): #Para todo el texto
       desp = get_desp(clave[i % len(clave)]) #Desplazamiento asociado a la letra clave
       result +=(ca.encryptC(text[i],desp)) #Ciframos la letra con caesar
    print("Cifrado\n")
    return result
    print()
