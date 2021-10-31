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

        return message_encrypted
    
    def decriptar(file='encriptacion.txt', block_size=2):


        openfile = open('private_keys.txt', 'r')
        re = str(openfile.readline())

        re = base64.b64decode(re).decode('utf-8')
        re = re.split('.')

        n = int(re[0])
        d = int(re[1])

        openfile.close()
        file = open('encriptacion.txt', 'r')
        file2 = str(file.readline())
        openfile.close()
        file.close()
        blocks = base64.b64decode('MzQ0MjEuMTIyMA==').decode('utf-8')
        print(blocks)
        list_blocks = blocks.split('.')

        int_blocks = []

        for s in list_blocks:
            int_blocks.append(int(s))

        txt = ""

        for i in range(len(int_blocks)):

            int_blocks[i] = (int_blocks[i]**d) % n

            tmp = ""

            for c in range(block_size):
                tmp = chr(int_blocks[i] % 1000) + tmp
                int_blocks[i] //= 1000
            txt += tmp

        print(txt)
        return txt
