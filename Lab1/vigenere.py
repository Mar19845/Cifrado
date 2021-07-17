def decryptV(text,clave):
    result = ""
    for i in range(0,len(text)): #Para todo el texto
        desp = get_desp(clave[i % len(clave)]) #Obtenemos el desplazamiento asociado a la clave
        result +=(caesar_decipher(text[i],desp)) #desciframos la letra con caesar para el desplazamiento dado
    print("Decifrado")
    return result


def encryptV(plain,clave):
    result = ""
    for i in range(0,len(plain)): #Para todo el texto
       desp = get_desp(clave[i % len(clave)]) #Desplazamiento asociado a la letra clave
       result +=(caesar_cipher(plain[i],desp)) #Ciframos la letra con caesar
       print("Cifrado")
    return result
