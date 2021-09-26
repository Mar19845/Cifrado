import mcd as m
def __init__():
    st = True
    while st:
        print("***Lab 7***")
        print("\n 1.Algoritmo de Euclides para calcular el MCD  \n 2.Algoritmo de Euclides para encontrar coeficientes X y Y \n 3.Hallar el inverso de a modulo n \n 4.Implemente el Test de primalidad de Fermat \n 5.Genere numeros primos \n 6.SALIR \n")
        opt = int(input("Elija alguna de las opciones:  \n" ))
        if opt == 1:
            print('\n')
            lista = [(1036,240),(22896,192),(689161,378851)]
            for i in lista:
                print('El mcd entre ',i[0],' ',i[1],' es: ',m.mcd(i[0],i[1]))
            print('\n')
        if opt == 2:
            print('\n')
            lista = [(1036,240),(8753,3354),(2021,43)]
            for i in lista:
                _,x,y= m.egcd(*i)
                print('Los coeficientes del mcd entre ',*i,' son: ', x,',',y)
            print('\n')
        if opt == 3:
            print('\n')
            lista = [(47,2020),(31,1234),(65,17316)]
            for i in lista:
                print('El inverso de ',i[0],' modulo ',i[1],' es: ',m.inverso_multi(i[0],i[1]))
            print('\n')
        if opt == 4:
            print('\n')
            lista =[1317, 2709, 3257, 3911, 4279, 5497, 6311, 7223, 8431, 9203]
            for i in lista:
                if m.fermat_test(i) == True:
                    print('El numero ',i,' es un numero primo')
                else:
                    print('El numero ',i,' no es un numero primo')
            print('\n')
        if opt == 5:
            pass
        if opt == 6:
            print("\n***** FIN DEL PROGRAMA *****\n")
            st = False
        if opt<1 or opt>6:
            print("\nOpción no valida, intente de nuevo\n")

if __name__ == "__main__":
    __init__()