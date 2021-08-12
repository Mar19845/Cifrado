import lcg as lcg
import lfsr as lfsr
def __init__():
    st = True
    while st:
        print("\n 1.LCG  \n 2.LFSR  \n 3.Wichman-Hill generator  \n 4.Image to btis \n 5.SALIR\n")
        opt = int(input("Elija el metodo que desea utilizar: " ))
        if opt == 1:
            n = lcg.init_lcg(5)
            print(n)
        if opt == 2:
            lfsr.lfsr(9, [4, 2, 5], 6)
        if opt == 3:
            pass
        if opt == 4:
            pass
        if opt == 5:
            print("\n***** FIN DEL PROGRAMA *****\n")
            st = False
        if opt<1 or opt>5:
            print("\nOpción no valida, intente de nuevo\n")
            
if __name__ == "__main__":
    __init__()