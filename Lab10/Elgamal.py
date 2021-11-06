import random
from math import pow
import base64
from lib import *

def gen_keys(minn=10000, maxx=100000):
    q = random.randint(minn, maxx)
    g = random.randint(2, q)
    
    key = random.randint(minn, q)
    while gcd(q, key) != 1:
        key = random.randint(minn, q)
    h = power(g, key, q)
    
    #encode private key and save it on txt fiel
    key = str(key).encode('utf-8')
    key = base64.b64encode(key).decode()
    f_private = open('private_key.txt', 'w')
    f_private.write(str(key))
    f_private.close()
    
    #encode public key g
    g = str(g).encode('utf-8')
    g = base64.b64encode(g).decode()
    #encode public key h
    h = str(h).encode('utf-8')
    h = base64.b64encode(h).decode()
    
    q = str(q).encode('utf-8')
    q = base64.b64encode(q).decode()
    #return public key
    
    f_public=open('public_key.txt', 'w')
    f_public.write(q+','+g+','+h)
    return q,g,h
#decode 
#g=base64.b64decode(g).decode('utf-8')

def encrypt(message):
    #get public key
    public_key=open('public_key.txt', 'r')
    pkeys = public_key.readline()
    q,g,h = pkeys.split(',')
    public_key.close()
    #get private key
    private_key=open('private_key.txt', 'r')
    key = private_key.readline()
    private_key.close()
    
    #decode private key and public keys
    q=int(base64.b64decode(q).decode('utf-8'))
    g=int(base64.b64decode(g).decode('utf-8'))
    h=int(base64.b64decode(h).decode('utf-8'))
    
    key=int(base64.b64decode(key).decode('utf-8'))
    #generate g^k and g^ak
    s = power(h, key, q)
    p = power(g, key, q)
    
    #encode p
    p = str(p).encode('utf-8')
    p = base64.b64encode(p).decode()
    msg = []
    for i in range(0, len(message)):
        msg.append(message[i])
    for i in range(0, len(msg)):
        cipher = s * ord(msg[i])
        cipher = str(cipher).encode('utf-8')
        cipher = base64.b64encode(cipher).decode()
        msg[i] = cipher
    
    #concatenan cipher text
    textC = ''
    for i in msg:
        textC = textC + i + ' '  
        
    #write cryptic text
    f_public=open('encrypt_msg.txt', 'w')
    f_public.write(textC + ',' + p)
    return textC,p

def decrypt(dirreccion='encrypt_msg.txt'):
    #get cryptic msg and key
    msg=open(dirreccion, 'r')
    pkeys = msg.readline()
    message,p= pkeys.split(' ,')
    #get public key
    public_key=open('public_key.txt', 'r')
    pkeys = public_key.readline()
    q,_,_ = pkeys.split(',')
    public_key.close()
    #get private key
    private_key=open('private_key.txt', 'r')
    key = private_key.readline()
    private_key.close()
    
    message=message.split(' ')
    #decode private key and public keys
    q=int(base64.b64decode(q).decode('utf-8'))
    p=int(base64.b64decode(p).decode('utf-8'))
    key=int(base64.b64decode(key).decode('utf-8'))
    decryptMsg = []
    h = power(p, key, q)
    for i in range(0, len(message)):
        message[i]=int(base64.b64decode(message[i]).decode('utf-8'))
        decryptMsg.append(chr(int(message[i]/h)))
        
    #write message decrypt
    decryptText=open('decrypt_msg.txt', 'w')
    decryptText.write(listJoiner(decryptMsg,""))
    
    return listJoiner(decryptMsg,"")



