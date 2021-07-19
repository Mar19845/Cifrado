import functionality as func
import matplotlib.pyplot as plt

alpha = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

def dencryptC(mensaje, desp):
    
    text=func.cleanTxt(mensaje)
    cipher = ''
    for i in text:
        suma = alpha.find(i) - desp
        modulo = int(suma) % len(alpha)
        
        cipher += str(alpha[modulo])
        
    
    return cipher


def caesar_brute(text):
   for i in range(26):
      print(chr(65+i)+": "+dencryptC(text,i))




def distribucion():
    mensaje = input("Ingrese un texto Cifrado o descrifrado: ")
    mensaje = func.cleanTxt(mensaje)
    dist = {
        'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'Ñ':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0
    }
    for i in mensaje:
        for j in alpha:
            if i==j:
                dist[i]=dist.get(i) + 1
    
    for i in dist:
        dist[i]= float(dist.get(i)/len(mensaje))

    return dist

def metica(dist):
    freq = {
        'A':0.11525,'B':0.02215,'C':0.04019,'D':0.05010,'E':0.12181,'F':0.00692,'G':0.01768,'H':0.00703,'I':0.06247,'J':0.00493,'K':0.00011,'L':0.04967,'M':0.03157,'N':0.06712,'Ñ':0.0311,'O':0.08683,'P':0.02510,'Q':0.00877,'R':0.06871,'S':0.07977,'T':0.04632,'U':0.02927,'V':0.01138,'W':0.00017,'X':0.00215,'Y':0.01008,'Z':0.00467
    }

    

    plt.figure(1)
    plt.subplot(211)
    plt.plot(list(freq.keys()),list(freq.values()),label='Teorico',color='red')
    plt.ylabel('Frecuencias')
    plt.legend()
    plt.subplot(212)
    plt.plot(list(dist.keys()),list(dist.values()),label='Experimental')


    plt.ylabel('Frecuencias')
    plt.legend()
    plt.show()

    
    


s=dencryptC('WDSFSDALALIHKXKWUNWFUASLISKSVWLUAXKSKUKAIMHYKSESLLWTSLSWFWLMNVASKDSXKWUNWFUASUHFDSJNWSISKWUWFDHLVALMAFMHLLAETHDHLWFNFDWFYNSBWVWMWKEAFSVHQDNWYHWLMNVASKDSXKWUNWFUASUHFDSJNWSISKWUWFWFDHLUKAIMHYKSESLQVWWLMSESFWKSWLMSTDWUWKNFSKWDSUAHFQHTMWFWKWDMWPMHIDSFHDSAVWSXNFVSEWFMSDWLJNWFHMHVSLDSLDWMKSLSISKWUWFUHFDSEALESXKWUNWFUASWFDHLMWPMHLLAFHJNWSDYNFSLSISKWUWFESLSEWFNVHJNWHMKSLUHFMSFVHDSLLAYFHLVWDMWPMHUAXKSVHQHKVWFSFVHDHLVWESQHKSEWFHKXKWUNWFUASIHVWEHLWLMSTDWUWKUHFBWMNKSLSUWKUSVWJNWDWMKSUHKKWLIHFVWSUSVSLAYFHWDSFSDALALLWUHEIDWMSUHFDSTNLJNWVSVWISDSTKSLXKWUNWFMWLUHEHSKMAUNDHLQIKWIHLAUAHFWLLASVWESLUHFHUWEHLHLHLIWUZSEHLVWSDYNFSISDSTKSJNWVWTSSISKWUWKWFWDEWFLSBWEWBHKJNWEWBHKWDKWLMHWLUNWLMAHFVWAFMNAUAHFLWYNFNFWLMNVAHLHTKWMWPMHLVWDVASKAHWDISALVWWFKAJNWXHFMSFADDHDSENWLMKSMHESVSVLHFDHLWBWEIDSKWLVWVAUZHVASKAHINTDAUSVHLVNKSFMWNFSLWESFSUAFUNWFMSQVHLEADLWALUAWFMHLVAWUAFNWÑWDWMKSLWFMHMSDDSXKWUNWFUASVWDSLDWMKSLWFUSLMWDDSFHWLSIKHPAESVSEWFMWDSJNWLAYNW'
,19)
print(s)
#metica(distribucion())