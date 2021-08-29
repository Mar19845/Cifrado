import AESencryption as aes
import Rutinas as rut
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
            aes.Ejercicio1()
        if opt == 2:
            print("\t\t1) Encriptar (mensaje1)")
            print("\t\t2) Encriptar (mensaje2)")
            print("\t\t3) Encriptar (mensaje3)")
            print("\t\t4) regresar a menu principal")
            opci=int(input("Ingrese una opcion: "))
            try:
                if opci == 1:
                    f = open ('mensaje1.txt','r')
                    mensaje = f.read()
                    print("El mensaje a encriptar sera: /n", mensaje)
                    rut.StringToBytes(mensaje)
                elif opci == 2:
                    f = open ('mensaje2.txt','r')
                    mensaje = f.read()
                    print("El mensaje a encriptar sera: /n", mensaje)
                    rut.StringToBytes(mensaje)
                elif opci == 3:
                    f = open ('mensaje3.txt','r')
                    mensaje = f.read()
                    print("El mensaje a encriptar sera: /n", mensaje)
                    rut.StringToBytes(mensaje)
                elif opci == 4:
                    print("regresar a menu principal")
                else:
                    print('opcion no valida')
            except ValueError:
                print('Por favor, ingresar numeros enteros') 
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
