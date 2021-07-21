import functionality as func

alpha = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'


def encryptC(mensaje, desp):
    
    text=func.cleanTxt(mensaje)
    cipher = ''
    for i in text:
        suma = alpha.find(i) + desp
        modulo = int(suma) % len(alpha)
        cipher += str(alpha[modulo])
    
    return cipher

def decryptC(mensaje, desp):
    
    text=func.cleanTxt(mensaje)
    cipher = ''
    for i in text:
        suma = alpha.find(i) - desp
        modulo = int(suma) % len(alpha)
        
        cipher += str(alpha[modulo])
        
    
    return cipher