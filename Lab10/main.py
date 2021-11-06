# Universidad del Valle de Guatemala
# Criptografia y cifrado de información
# Laboratorio #9
# Eduardo Ramírez Herrera 19946
# Juan Manuel Marroquin 19845
# Carlos Ráxtum 19721

from Elgamal import *


def __init__():

    st = True
    finish_program = False

    while(st):
        print("\n***LABORATORIO 10***\n")
        print("Cifrado Elgamal:\n 1. Generar Claves\n 2. Encriptar mensaje\n 3. Decriptar mensaje\n 4. Salir\n")
        opt = input("Elija la funcion que desea ejecutar: ")

        if opt == "1":
            gen_keys()
            print('Claves generadas revisar archivos en directorio')

        elif opt == "2":
            txt = input("Ingrese el texto que desea encriptar: ")

            encrypt(txt)
            print('Mensaje encriptado revisar archivo en directorio')

        elif opt == "3":
            txt = input("Ingrese el nombre del archivo que desea desencriptar o presione eneter para utilizar el que se encuntra en el directorio: ")
            if len(txt) == 0:
                decrypt()
            else:
                decrypt(txt)
            print('Mensaje decriptado revisar archivo en directorio')

        elif opt == "4":
            print("\n*** FIN DEL PROGRAMA ***")
            st = finish_program
            
if __name__ == "__main__":
    __init__()
