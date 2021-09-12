import password_manager as pm

def __init__():
    st = True
    while st:
        print("***Lab 5***")
        print("\n 1.Implementar los cifrados sha256, sha512 y blake2b.  \n 2.Simular con las rutinas del ejercicio 1  \n 3.Simular un manejador de passwords  \n 4.SALIR\n")
        opt = int(input("Elija alguna de las opciones:  \n" ))
        if opt == 1:
            print('Implementar los cifrados sha256, sha512 y blake2b.')
        if opt == 2:
            print('Simular con las rutinas del ejercicio 1')
        if opt == 3:
            pmvar=True
            while pmvar:
                print("\n 1.Login \n 2.Register \n 3.Salir \n")
                option=int(input("Elija alguna de las opciones:  \n" ))
                if option ==1:
                    username,password=pm.ask_data()
                    login=pm.login(username, password)
                    if login==True:
                        print('LOGUEADO %s'%username)
                    elif login==False:
                        print('Algo ingreso mal')
                if option == 2:
                    username,password=pm.ask_data()
                    pm.register(username, password)
                if option ==3:
                    pmvar=False
                if opt<1 or opt>3:
                    print("\nOpción no valida, intente de nuevo\n")
        if opt == 4:
            print("\n***** FIN DEL PROGRAMA *****\n")
            st = False
        if opt<1 or opt>4:
            print("\nOpción no valida, intente de nuevo\n")

if __name__ == "__main__":
    __init__()