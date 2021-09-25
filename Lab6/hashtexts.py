import hashlib

original_file = open("texto.txt", "r")
mensaje = original_file.read()
new_message = mensaje.replace("a", "d")  
copy_file = open("texto2.txt", "w+")
copy_file.write(new_message + "\n")
original_file.close()
copy_file.close()

def hashGenerator(filename, password):
    try:
        original_file = open(filename, "r")
        mensaje = original_file.read()
        mensaje = bytes(mensaje, 'utf-8')
        password = bytes(password, 'utf-8')
        hash = hashlib.sha256()
        hash.update(mensaje)
        hash.update(password)
        result = hash.hexdigest()
        compareFile = open("comparar.txt", "a+")
        compareFile.write(result + "\n")
        original_file.close()
        compareFile.close()
    except OSError:
        print("Could not open/read file:", filename)
    print("Hash generado ")




