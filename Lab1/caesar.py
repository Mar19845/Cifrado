import functionality as func

def encryptC(mensaje, desp):
    
    text=func.cleanTxt(mensaje)
    cipher = ''
    for i in range(len(mensaje)):
        char = text[i]
        if (char.islower()):
            cipher += chr((ord(char) + desp - 97) % 26 + 97)  # 97 letra minuscula (a)
        else:
            cipher += chr((ord(char) + desp - 65) % 26 + 65)  # Prima letra mayuscula (A)
    
    print("DESENCRIPTADO\n")
    return cipher

def decryptC(mensaje, desp):
    
    desp = mensaje
    text=func.cleanTxt(mensaje)
    plain = ""
    for i in range(len(mensaje)):
        char = text[i]
        if (char.islower()):
            plain += chr((ord(char) -97-desp) % 26 + 97)
        else:
            plain += chr((ord(char) -65-desp) % 26 + 65)
    
    print("ENCRIPTADO\n")
    return plain