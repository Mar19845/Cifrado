import hashlib
import os
from hashlib import blake2b

# Calculate the first hash with a random salt.
salt1 = os.urandom(blake2b.SALT_SIZE)
mensaje='este es un mensaje mas largo'
x=hashlib.sha256(b"me")
#print(x.hexdigest())

#dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
#print(dk.hex())
b = str.encode(mensaje)
b1= str.encode(mensaje)
dk = hashlib.pbkdf2_hmac('sha256', b, salt1, 100000)
print(dk.hex())
dk1 = hashlib.pbkdf2_hmac('sha256', b1, salt1, 100000)
if dk.hex()==dk1.hex():
    print('to funciona pa')
else:
    print('no funciona pa')