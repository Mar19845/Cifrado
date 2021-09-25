import password_manager as pm
#import hashtexts as ht
import hashlib
import codecs

def __init__():
    st = True
    while st:
        print("***Lab 6***")
        print("\n 1.Implementar los cifrados sha256, sha512 y blake2b.  \n 2.Simular con las rutinas del ejercicio 1  \n 3.Simular un manejador de passwords  \n 4.SALIR\n")
        opt = int(input("Elija alguna de las opciones:  \n" ))
        if opt == 1:

            texto = input("Ingrese el texto a cifrar:\n")
            convertir = bytes(texto, 'utf-8')

            print('Implementar los cifrados sha256, sha512 y blake2b.\n')
            #----------------------------------------------
            print('cifrado sha256')
            m = hashlib.sha256(convertir)
            print('mensaje en hash binario', m.digest())
            print('mensaje en hexadecimal', m.hexdigest())
            result = codecs.encode(hashlib.sha256(convertir).digest(), 'base64')
            print('mensaje en Base64', result, '\n')
           # print('mensaje en Base64', base64.b64encode(hashlib.sha256("test").digest()))
            
            #----------------------------------------------
            print('cifrado sha512')
            m = hashlib.sha512(convertir)
            print('mensaje en hash binario', m.digest())
            print('mensaje en hexadecimal', m.hexdigest())
            result = codecs.encode(hashlib.sha512(convertir).digest(), 'base64')
            print('mensaje en Base64', result, '\n')
            #----------------------------------------------
            print('cifrado blake2b')
            m = hashlib.blake2b(digest_size = 15)
            m.update(convertir)  
            result = m.digest()
            print('mensaje en hash binario', result)
            print('mensaje en hexadecimal', m.hexdigest())   
            result2 = codecs.encode(result, 'base64')
            print('mensaje en Base64', result2, '\n')
            
        if opt == 2:
            print('Simular con las rutinas del ejercicio 1')
           # filename = input("Ingrese el archivo al que desee generar hash (texto.txt):\n")
           # password = input("ingrese la clave del archivo:\n")
           # ht.hashGenerator(filename, password)
        


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