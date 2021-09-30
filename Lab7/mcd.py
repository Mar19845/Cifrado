import random
def primo(num): #funcion para verificar Num primos
    contador = 0
    if num < 2:
        return False
    
    for i in range (2, num):
        if num % i == 0:
            return False
        
    return True


#Ejercicio 1
#algoritmo de euclides para el mcd
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#funcion para el inverso multiplicativo
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


#Ejercicio 3
#algoritmo de euclides extendido para encontrar el inverso multiplicativo de dos numeros
def inverso_multi(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        return False
    else:
        return x % phi

#Ejercicio 4
#algoritmo de realizar el test de fermat
#tomado de: https://gist.github.com/Ayrx/5884802

def power(a, n, p):
     
    res = 1
     
    a = a % p 
     
    while n > 0:
         

        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
             
            n = n // 2
             
    return res % p

def fermat_test(n, k=5):

    # Implementation uses the Fermat Primality Test
    
    # If number is even, it's a composite number

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(k):
        a = random.randint(2, n - 2)
             
        # Fermat's little theorem
        if power(a, n - 1, n) != 1:
            return False
                 
    return True
