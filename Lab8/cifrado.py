from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

def encrypt_cbc(key, message):
    message = message.encode('ascii')
    cipher = AES.new(key, AES.MODE_CBC)
    cipherbytes = cipher.encrypt(pad(message, AES.block_size))
    iv = b64encode(cipher.iv).decode("utf-8")
    ciphertext = b64encode(cipherbytes).decode("utf-8")
    #print("Encrypted:", ciphertext)
    return iv, ciphertext


def decrypt_cbc(key, iv, message):
    try:
        iv = b64decode(iv)
        ciphertext = b64decode(message)
        decript = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(decript.decrypt(ciphertext), AES.block_size)
        plaintext = plaintext.decode("utf-8")
        
        print("Decrypted:", plaintext)
       # return plaintext
    except:
        # print("Decryption failed")
        return "Decryption failed"
        
'''   
#AES usando python
from Crypto.Cipher import AES

def encrypt(key, data):
    
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    print("Mensaje encriptado")
    return cipher.nonce + tag + ciphertext

def decrypt(key, data):
    nonce = data[:AES.block_size]
    tag = data[AES.block_size:AES.block_size * 2]
    ciphertext = data[AES.block_size * 2:]

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    
    return cipher.decrypt_and_verify(ciphertext, tag)'''