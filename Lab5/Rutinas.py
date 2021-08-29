import AESencryption as aes
#funcion de texto a hexadecimal
def StringToHex(text):
    s= text.encode('utf-8')
    print(s.hex())

#funcion de texto a hexadecimal
def StringToBytes(string):
    # texto con encoding 'utf-8'
    arr = bytes(string, 'utf-8')
    #print(arr,'\n')
    print("\n 1.CTR AES  \n 2.CBC  \n 3.OFB  \n 4.SALIR\n")
    opt = int(input("Elija alguna de las opciones:  \n" ))
    try:
        if opt == 1:
            aes.CTRmode(arr) 
        elif opt == 2:
            aes.CBCmode(arr)
        elif opt == 3:
            aes.OFBmode(arr)
        elif opt == 4:
            print("regresar a menu principal")
        else:
            print('opcion no valida')
    except ValueError:
        print('Por favor, ingresar numeros enteros')

def HexToString (hex):
    #"68656c6c6f" example 
    #53616d706c6520537472696e67 example2
    #string = "68656c6c6f"
    byte_array = bytearray.fromhex(hex)
    print(byte_array.decode())

def BytesToString(bytes):
# Let's check the type
    type(bytes)
# Now, let's decode/convert them into a string
    s = bytes.decode('UTF-8')
    print(s)
#BytesToString(b"Lets eat a \xf0\x9f\x8d\x95!"  )

