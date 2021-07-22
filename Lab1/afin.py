
import functionality as func
import vigenere as vi
from itertools import *
import numpy as np 
import nltk
import re

class afinCypher:

    def __init__(self, alphabet, tprob):
            self.alphabet = alphabet
            self.tprob = tprob

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

    def decryptV(self, key, text):
        key_array = [key[i % len(key)].upper() for i in range(len(text))]
        return ''.join(
            self.abc[
                (self.abc.index(text[i]) - self.abc.index(key_array[i]))
                % len(self.abc)
            ]
            for i in range(len(text))
        )
    def probabilidad(self, text):
        text = func.cleanTxt(text)
        tokens = re.findall('.', text)
        freq = nltk.FreqDist(tokens)
        freq = freq.most_common(len(self.alphabet))
        freq_array = [i[1] for i in freq]
        freq_array = np.array(freq_array)
        p = freq_array / freq_array.sum()
        prob = {l[0]: p[count] for count, l in enumerate(freq)}
        for l in self.alphabet:
            if l not in prob:
                prob[l] = 0
        return {l: prob[l] for l in self.alphabet}

    def fuerzabrutaAfin(self, text):
            key = []
            for i in range(len(self.alphabet)):
                for j in range(len(self.alphabet)):
                    a = self.encryptA(i, j, text)
                    b = self.probabilidad(a)
                    metric = self.metrica(self.tprob, b)
                    abs_error = sum(value for key, value in metric.items())
                    key.append((i, j, abs_error))
            better = sorted(key, key=lambda x: x[2])[0][0:2]
            return self.encryptA(better[0], better[1], text), better

    def metrica(self, teoric, textProb):
        return {l: abs(teoric[l] - textProb[l]) for l in self.alphabet}
    
    
    def fuerzabrutaV(self, text):
        keys = []
        options_keys = []
        for i in range(5):
            a = list(product(self.alphabet, repeat=i))
            for j in a:
                b = "".join(j)
                c = 'abv'
                try:
                    c = self.decryptV(b, text)
                except:
                    c = 'abv'
                d = self.probabilidad(c)
                metric = self.metrica(self.tprob, d)
                abs_error = sum(value for key, value in metric.items())
                keys.append((b, abs_error))
        better = sorted(keys, key=lambda x: x[1])[0][0]
        return self.decryptV(better, text), better
