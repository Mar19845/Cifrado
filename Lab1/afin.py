
import functionality as func


class afinCypher:
    def __init__(self, alphabet):
            self.alphabet = alphabet
            

    def encryptA(self, a, b, message):

        text=func.cleanTxt(message)
        return "".join(self.alphabet[(self.alphabet.index(l)*a + b) % len(self.alphabet)] for l in text)

    def decryptA(self, a, b, message):

        text=func.cleanTxt(message)
        return "".join(self.alphabet[(int((self.alphabet.index(l) - b) * self.inverso(a, len(self.alphabet)))) % len(self.alphabet)] for l in text)
    
    def inverso(self, a, m):
        g, x, y = self.euc_alg(a, m)
        if g != 1:
            raise Exception('No existe el inverso modular!')
        else:
            return x % m

    def euc_alg(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = self.euc_alg(b % a, a)
            return (g, y - (b // a) * x, x)       