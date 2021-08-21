import AESencryption as aes

def __init__():
    st = True
    while st:
        print("***Lab 5***")
        print("\n 1.CIfrado AES  \n 2.rutinas AES.encrypt() y AES.decrypt()  \n 3.Encriptar archivos de teto con AES  \n 4.SALIR\n")
        opt = int(input("Elija alguna de las opciones: " ))
        if opt == 1:
            aes.encryption()
        if opt == 2:
            pass
        if opt == 3:
            pass
        if opt == 4:
            print("\n***** FIN DEL PROGRAMA *****\n")
            st = False
        if opt<1 or opt>4:
            print("\nOpción no valida, intente de nuevo\n")

if __name__ == "__main__":
    __init__()








