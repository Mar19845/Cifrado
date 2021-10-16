
import pyDH
import hmac
import hashlib
import fermat as fmt
import cifrado as cf
#resultado d1 <pyDH.pyDH.DiffieHellman object at 0x0000020D54A7FEE0>
#predefrnir un  primo y construir un generador d1 calcula la potencia de g a la a
#21386147990689131804096242191407514178416222066674015765170288757534116532363069306733944479239361060908992703541019452422084394434144806779527717713304082138997521446417056706092161419985004750107721206072326255181446626489180822438777606951364274024220436300546991857498775648799709495523295209822723449900748133163494013526881853433037438367395827146178077246069329672344173059383061351671823789974675022642905554520841087674044262062401162322026640221128434469128157107935355861006743038715050725793299493425711715205766671412633426029421771728587176287891603738944375435439057333244225229525180498827415679796136
def pyDHgenerador():
    d1 = pyDH.DiffieHellman(14)
    #d2 = pyDH.DiffieHellman(14)
    d1_pubkey = d1.gen_public_key()
    #d2_pubkey = d2.gen_public_key()
    print(d1_pubkey)
    print('\n')
    d2_pubkey=int(input('ingrese llave del otro tim: '))
    #generar la clave secreta con la otra
    d1_sharedkey = d1.gen_shared_key(d2_pubkey)
    return d1_sharedkey
'''
import random
from random import randint


def Diffie_Hellman(n=2):
    data = "Solo hay una pregunta que nadie podrá responder afirmativamente y diciendo la verdad. ¿Estas dormido?"
    
    p = 29996224275833
    q = 3695229511810
    #private keys
    A_private_key = randint(2,p-1)
    #B_private_key = randint(1,p-1)
    A_public_key = p**A_private_key % q
    print("Esta llave publica se comparte al otro grupo", A_public_key)

    #B_public_key = p**B_private_key % q
    B_public_key = int(input("Ingrese la llave publica del otro grupo "))
    #calc a and b same keys

    A = B_public_key**A_private_key % q
    #B = A_public_key**B_private_key % q
    #return A #(), B) Retornamos el sharekey, esta debe ser la misma al otro grupo
    A = (str(A))
    print (A)

    data1 = bytes(data, 'utf-8')
    key1 = bytes(A, 'utf-8')
    cf.encrypt(key1, data1)
'''

