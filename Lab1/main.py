# Universidad del Valle de Guatemala
# Cifrado de Información
# Lab #1
# Juan Manuel Marroquin 19845
# Eduardo Ramírez Herrera 19946
# Carlos Ráxtum 19721

from functionality import *

st = True

print("*****ANALISIS DE FUERZA BRUTA*****\n")
while(st):
    print(" 1.Caesar \n 2.Afín \n 3.Vigenère\n 4.Distribuciones\n 5.SALIR\n")
    opt = int(input("Elija el metodo que desea utilizar: " ))

    if opt == 1:

        print("\n*****CAESAR METHOD*****\n")
        caesarInit()

    if opt == 2:
        
        print("\n*****AFIN METHOD*****\n")
        afinInit()

    if opt == 3:
        
        print("\n*****VIGENERE METHOD*****\n")
        vigenereInit()
    if opt == 4:
        
        print("\n*****DISTRIBUCCION*****\n")
        distribucion()
    if opt == 5:
        
        print("\n*****FIN DEL PROGRAMA*****\n")
        st = False

    if opt<1 or opt>5:
        print("\nOpción no valida, intente de nuevo\n")
        
    