'''
from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key()
file_out = open("receiver.pem", "wb")
file_out.write(public_key)
file_out.close()
'''
import json
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def CTRmode():
    data = b"secret"
    key = get_random_bytes(16) 
    cipher = AES.new(key, AES.MODE_CTR)
    ct_bytes = cipher.encrypt(data)
    nonce = b64encode(cipher.nonce).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'nonce':nonce, 'ciphertext':ct})
    print("Mensaje encriptado por CTR")
    print(result)
    print("")

    try:
        b64 = json.loads(result)
        nonce = b64decode(b64['nonce'])
        ct = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
        pt = cipher.decrypt(ct)
        print("Mensaje desencriptado por CTR")
        print("The message was: ", pt)
        print("")
    except ValueError or KeyError:
        print("Incorrect decryption")
        print("")

def CFBmode():
    data = b"secret"
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CFB)
    ct_bytes = cipher.encrypt(data)
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv':iv, 'ciphertext':ct})
    print("Mensaje encriptado por CFB")
    print(result)
    print("")

    try:
        b64 = json.loads(result)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_OFB, iv=iv)
        pt = cipher.decrypt(ct)
        print("Mensaje desencriptado por CFB")
        print("The message was: ", pt)
        print("")
    except ValueError or KeyError:
        print("Incorrect decryption")
        print("")


def OFBmode():
    data = b"secret"
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_OFB)
    ct_bytes = cipher.encrypt(data)
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv':iv, 'ciphertext':ct})
    print("Mensaje encriptado por OFB")
    print(result)
    print("")

    try:
        b64 = json.loads(result)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_OFB, iv=iv)
        pt = cipher.decrypt(ct)
        print("Mensaje desencriptado por OFB")
        print("The message was: ", pt)
        print("")
    except ValueError or KeyError:
        print("Incorrect decryption")
        print("")




