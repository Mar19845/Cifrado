import caesar as ca
import functionality as func

def decryptV(text,clave):
    result = ""
    for i in range(0,len(text)): #Para todo el texto
        desp = get_des(clave[i % len(clave)]) #Obtenemos el desplazamiento asociado a la clave
        result +=(ca.decryptC(text[i],desp)) #desciframos la letra con caesar para el desplazamiento dado
    print("Decifrado")
    return result


def encryptV(plain,clave):
    result = ""
    for i in range(0,len(plain)): #Para todo el texto
       desp = get_des(clave[i % len(clave)]) #Desplazamiento asociado a la letra clave
       result +=(ca.encryptC(plain[i],desp)) #Ciframos la letra con caesar
       print("Cifrado")
    return result
