import AESencryption as aes
import encriptador as enc

import os
import os.path
from os import listdir
from os.path import isfile, join

def __init__():
    st = True
    while st:
        print("***Lab 5***")
        print("\n 1.CIfrado AES  \n 2.rutinas AES.encrypt() y AES.decrypt()  \n 3.Encriptar archivos de tetxo con AES  \n 4.SALIR\n")
        opt = int(input("Elija alguna de las opciones:  \n" ))
        if opt == 1:
            aes.CTRmode() 
            aes.CFBmode()
            aes.OFBmode()
        if opt == 2:
            print("\t\t1) Encriptar por cadena de texto")
            print("\t\t2) Encriptar por bytes")
            print("\t\t3) Encriptar por Hex")
            print("\t\t4) regresar a menu principal")
            opci=int(input("Ingrese una opcion: "))
            try:
                if opci == 1:
                    val = input("Ingrese la cadena de texto: ")
                elif opci == 2:
                    val = input("Ingrese bytes: ")
                elif opci == 3:
                    val = input("Ingrese Hex: ")
                elif opci == 4:
                    print("regresar a menu principal")
                else:
                    print('opcion no valida')
            except ValueError:
                print('Por favor, ingresar numeros enteros')
                print("")
                
        if opt == 3:
            key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
            clear = lambda: os.system('cls')
            ruta = input("Ingrese el nombre del archivo (debe de estar en la misma carpeta que este codigo):  \n" )
            encodefile = enc.encrypt_file(ruta,key)
            input('Presione enter para decriptar el archivo\n')
            enc.decrypt_file(encodefile,key)
            
        if opt == 4:
            print("\n***** FIN DEL PROGRAMA *****\n")
            st = False
        if opt<1 or opt>4:
            print("\nOpción no valida, intente de nuevo\n")

if __name__ == "__main__":
    __init__()








