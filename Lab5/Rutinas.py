
#funcion de texto a hexadecimal
def StringToHex(text):
    s= text.encode('utf-8')
    print(s.hex())

#funcion de texto a hexadecimal
def StringToBytes(string):
    # texto con encoding 'utf-8'
    arr = bytes(string, 'utf-8')
    print(arr,'\n')
    # actual bytes en el texto
    for byte in arr:
        print(byte, end=' ')
    print("\n")

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
BytesToString(b"Lets eat a \xf0\x9f\x8d\x95!"  )

