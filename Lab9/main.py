# Universidad del Valle de Guatemala
# Criptografia y cifrado de información
# Laboratorio #9
# Eduardo Ramírez Herrera 19946
# Juan Manuel Marroquin 19845
# Carlos Ráxtum 19721

from RSA import cipherRSA


def __init__():

    st = True
    finish_program = False

    while(st):
        print("\n***LABORATORIO 9***\n")
        print("Cifrado RSA:\n 1. Generar Claves\n 2. Encriptar mensaje\n 3. Decriptar mensaje\n 4. Salir\n")
        opt = input("Elija la funcion que desea ejecutar: ")

        if opt == "1":
            cipherRSA.generarClaves()

        elif opt == "2":
            txt = input("Ingrese el texto que desea encriptar: ")

            cipherRSA.encriptar(txt)

            a = cipherRSA.encriptar(txt)

            print(a)

        elif opt == "3":
            txt = input("Ingrese el nombre del archivo que desea desencriptar: ")
            cipherRSA.decriptar(txt)

            a = cipherRSA.decriptar(txt)
            print(a)

        elif opt == "4":
            print("\n*** FIN DEL PROGRAMA ***")
            st = finish_program
            
if __name__ == "__main__":
    __init__()
