import dh as d
def __init__():
    st = True
    while st:
        print("***Lab 8***")
        print("\n 1.Simular un intercambio de claves usando el algoritmo de Diffie-Hellman  \n 2.Intercambio con Otro equipo \n 3.SALIR \n")
        opt = int(input("Elija alguna de las opciones:  " ))
        if opt == 1:
            n = int(input("Ingrese con cuantos digitos desea gener un numero Primo para p: "))
            A,B=d.Diffie_Hellman(n)
            print('\n Las claves de Alice y Bob son : '+ str(A) + ' y '+str(B))
        if opt == 2:
            print('Ejercicio 2\n')
        if opt == 3:
            print("\n***** FIN DEL PROGRAMA *****\n")
            st = False
        if opt<1 or opt>3:
            print("\nOpción no valida, intente de nuevo\n")

if __name__ == "__main__":
    __init__()