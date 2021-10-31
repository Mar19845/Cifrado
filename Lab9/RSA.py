from generators import *


class cipherRSA:

    def generarClaves():
        print("*** Generar Claves ***\n")
        generar_clave()
    
    def encriptar(txt, public):

        re = base64.b64decode(public).decode('utf-8')
        re = re.split('.')

        e = int(re[0])
        n = int(re[1])

        st = []

        for ch in txt:
            val = power(ord(ch),e,n)
            st.append(chr(val))

        ciphertext = listJoiner(st, '')

        print(ciphertext)


        file_encrypted = open('encriptacion.txt', 'w')
        message_encrypted = base64.b64encode(bytes(ciphertext, 'utf-8'))
        message_encrypted = message_encrypted.decode('utf-8')
        file_encrypted.write(str(message_encrypted))
        file_encrypted.close()

        return message_encrypted
    
    def decriptar(ciphertxt):

        cipher = base64.b64decode(ciphertxt).decode('utf-8')

        d = 39389
        n = 68093

        st = []

        for ch in cipher:
            val = power(ord(ch),d,n)
            st.append(chr(val))

        decryptedtxt = listJoiner(st, '')

        return decryptedtxt
