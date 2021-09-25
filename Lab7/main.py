
def __init__():
    st = True
    while st:
        print("***Lab 6***")
        print("\n 1.Implementar los cifrados sha256, sha512 y blake2b.  \n 2.Simular con las rutinas del ejercicio 1  \n 3.Simular un manejador de passwords  \n 4.SALIR\n")
        opt = int(input("Elija alguna de las opciones:  \n" ))
        if opt == 1:
            pass
            
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