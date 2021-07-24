# Universidad del Valle de Guatemala
# Cifrado de Información
# Lab #2
# Juan Manuel Marroquin 19845
# Eduardo Ramírez Herrera 19946
# Carlos Ráxtum 19721

from cleaner import *
import charbits as cb

st = True

print("\n***** LABORATORIO #2 *****")
while(st):
    print("\n 1.Caracteres a Bits \n 2.Caracteres a Base64 \n 3.Operación XOR \n 4.SALIR \n")
    opt = int(input("Elija el metodo que desea utilizar: " ))

    if opt == 1:

        print("\n***** Char to Bits *****\n")
        phrase = input("Escriba algo: ")

        phrase = cleanTxt(phrase)
        val, translate = cb.toBits(phrase)

        print("\nCadena de caracteres a bits:", val)

        input("Presiona ENTER para mostrar la cadena de bits a caracteres")

        original = cb.toChar(translate)
        print("\nCadena de bits a caracteres:", original)

    if opt == 2:
        
        print("\n***** Char to Base64 *****\n")
        

    if opt == 3:
        
        print("\n***** XOR Operation *****\n")
        
    if opt == 4:
        
        print("\n***** FIN DEL PROGRAMA *****\n")
        st = False

    if opt<1 or opt>4:
        print("\nOpción no valida, intente de nuevo\n")
        
    