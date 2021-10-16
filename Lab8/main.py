import dh as d
import cifrado as cf
import pyDHparte2 as parte2
def __init__():
    st = True
    out = False
    while st:
        print("***Lab 8***")
        print("\n 1.Simular un intercambio de claves usando el algoritmo de Diffie-Hellman  \n 2. Ejercicio 2 Intercambio con tro equipo \n 3.SALIR \n")
        opt = int(input("Elija alguna de las opciones:  " ))

        if opt == 1:
            n = int(input("Ingrese con cuantos digitos desea gener un numero Primo para p: "))
            A,B=d.Diffie_Hellman(n)
            print('\n Las claves de Alice y Bob son : '+ str(A) + ' y '+str(B))
        if opt == 2:
            #soy uvg te ofrece la oportunidad de volver a conectar con antiguos amigos
            d1_sharedkey = parte2.pyDHgenerador()
            print("shared key: ", d1_sharedkey[0:16])
            print("shared key: ", bytes(d1_sharedkey[0:16], 'utf-8'))
            
            while out == False:
                print("\n 1.Encriptar \n 2. Descencriptar \n 3.SALIR \n")
                opt = int(input("Elija alguna de las opciones:  " ))
                if opt == 1 :
                    data = input("Ingrese el texto a cifrar ") 
                    data1 = bytes(data, 'utf-8')
                    key1 = bytes(d1_sharedkey[0:16], 'utf-8')
                    #print(key1)
                    #print(data1)
                    iv, ciphertext = cf.encrypt_cbc(key1, data)
                    print ("Mensaje encriptado: ",  ciphertext, "\n", "IV",  iv )

                elif opt == 2:
                    data = input("Ingrese el texto a descifrar ") 
                    print(d1_sharedkey[0:16])
                    ivteam = input("Ingresar el iv del otro equipo ")
                    message = cf.decrypt_cbc(bytes(d1_sharedkey[0:16], 'utf-8'),ivteam, data)
                    #print ("Mensaje encriptado: ",  message )
                elif opt == 3:
                    print("\n***** FIN DEL CIFRADO *****\n")
                    out = False
                    break
                else: 
                    print("Opcion no valida")
     
        if opt == 3:
            print("\n***** FIN DEL PROGRAMA *****\n")
            st = False
        if opt<1 or opt>3:
            print("\nOpción no valida, intente de nuevo\n")

if __name__ == "__main__":
    __init__()