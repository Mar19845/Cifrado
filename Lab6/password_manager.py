from pandas import DataFrame
import hashlib
import os
from hashlib import blake2b
def ask_data():
    username=input('Username: ') 
    password=input('Password: ')
    return username,password
#login function
def login(username, password):
    all_users=[]
    
    with open('passwords.txt','r') as f:
        lines = f.read().splitlines()
        for line in lines:
            user,salt,passwordD=line.split(',')
            userList=[user,salt,passwordD]
            salt=bytes.fromhex(salt)
            userList=[user,salt,passwordD]
            all_users.append(userList)
    df = DataFrame (all_users,columns=['username','salt','password'])
    df=df.loc[df['username'] == username]
    usercheck = df.values.tolist()
    if len(usercheck) == 0:
        print('User not found: %s'%username)
        return False
    else:
        pass
    usercheck=usercheck[0]
    dk = hashlib.pbkdf2_hmac('sha256',str.encode(password), usercheck[1], 100000)
    if usercheck[2]!=dk.hex():
        print('Password dont match')
        return False
    elif usercheck[2]==dk.hex():
        print('Match')
        return True
    
def register(username, password):
    with open('passwords.txt','a') as f:
        salt = os.urandom(blake2b.SALT_SIZE)
        dk = hashlib.pbkdf2_hmac('sha256',str.encode(password), salt, 100000)
        password = dk.hex()
        f.write('\n'+username+','+salt.hex()+','+password)
    print('Done!!')

