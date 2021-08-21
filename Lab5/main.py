import AESencryption as aes

def __init__():
    st = True
    while st:
        print("***Lab 5***")
        print("\n 1.CIfrado AES  \n 2.rutinas AES.encrypt() y AES.decrypt()  \n 3.Encriptar archivos de teto con AES  \n 4.SALIR\n")
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
            pass
        if opt == 4:
            print("\n***** FIN DEL PROGRAMA *****\n")
            st = False
        if opt<1 or opt>4:
            print("\nOpción no valida, intente de nuevo\n")

if __name__ == "__main__":
    __init__()








