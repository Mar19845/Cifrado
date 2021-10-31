from generators import *


class cipherRSA:

    def generarClaves():
        print("*** Generar Claves ***\n")
        generar_clave()
    
    def encriptar(txt, file_name='public_keys.txt', block_size=2):

        try:
            openfile = open(file_name, 'r')

        except FileNotFoundError:
            print('That file is not found.')
        else:
            re = str(openfile.readline())

        re = base64.b64decode(re).decode('utf-8')
        re = re.split('.')

        n = int(re[0])
        e = int(re[1])
        openfile.close()

        encrypted_blocks = []
        ciphertext = -1

        if (len(txt) > 0):

            ciphertext = ord(txt[0])

        for i in range(1, len(txt)):

            if (i % block_size == 0):
                encrypted_blocks.append(ciphertext)
                ciphertext = 0

            ciphertext = ciphertext * 1000 + ord(txt[i])

        encrypted_blocks.append(ciphertext)

        for i in range(len(encrypted_blocks)):
            encrypted_blocks[i] = str((encrypted_blocks[i]**e) % n)

        message_encrypted = ".".join(encrypted_blocks)
        file_encrypted = open('encriptacion.txt', 'w')
        print("El texto se ha cifrado y se genero un archivo")
        message_encrypted = base64.b64encode(bytes(message_encrypted, 'utf-8'))
        message_encrypted = message_encrypted.decode('utf-8')
        file_encrypted.write(str(message_encrypted))
        file_encrypted.close()

        return "El texto se ha cifrado y se genero un archivo"
    
    def decriptar():
        return 'x2'
