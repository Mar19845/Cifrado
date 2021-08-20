import lcg as lcg
import lfsr as lfsr
import WichmanHill as Wichman_Hill
import tests as test

def __init__():
    st = True
    while st:
        print("***NIST TESTS***")
        print("\n 1.LCG  \n 2.LFSR  \n 3.Wichman-Hill generator  \n 4.SALIR\n")
        opt = int(input("Elija el metodo que desea testear: " ))
        if opt == 1:
            length = int(input("ingrese el tamaño de la lista "))
            n = lcg.LCG(length)
            print(n)
            t = test.monobit(n, length)
            t1 = test.run(n, length)
            print(t)
            print(t1)


        if opt == 2:
            length = int(input("ingrese el tamaño de la lista "))
            lfsr.lfsr(9, [4, 2, 5], 6)
        if opt == 3:
            length = int(input("ingrese el tamaño de la lista "))
            print(Wichman_Hill.Wichmann_Hill(length))
    
        if opt == 4:
            print("\n***** FIN DEL PROGRAMA *****\n")
            st = False
        if opt<1 or opt>4:
            print("\nOpción no valida, intente de nuevo\n")

if __name__ == "__main__":
    __init__()