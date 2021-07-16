def encryptC():
    text=cleanTxt(text)
    cipher = ''
    for i in range(len(text)):
        char = text[i]
        if (char.islower()):
            cipher += chr((ord(char) + desp - 97) % 26 + 97)  # 97 letra minuscula (a)
        else:
            cipher += chr((ord(char) + desp-65) % 26 + 65)  # Prima letra mayuscula (A)
    
    print("DESENCRIPTADO\n")
    return cipher

def decryptC():
    text=cleanTxt(text)
    plain = ""
    for i in range(len(text)):
        char = text[i]
        if (char.islower()):
            plain += chr((ord(char) -97-desp) % 26 + 97)
        else:
            plain += chr((ord(char) -65-desp) % 26 + 65)
    
    print("ENCRIPTADO\n")
    return plain