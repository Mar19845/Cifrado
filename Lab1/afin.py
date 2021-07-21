
import functionality as func
from itertools import *
import numpy as np 
import nltk
import re


def __init__(self, abc):
        self.abc = abc
        

def encryptA(self, a, b, message):

    text=func.cleanTxt(message)
    return "".join(self.abc[(self.abc.index(l)*a + b) % len(self.abc)] for l in text)

def decryptA(self, a, b, message):

    text=func.cleanTxt(message)
    return "".join(self.abc[(int((self.abc.index(l) - b) * self.inv_mod(a, len(self.abc)))) % len(self.abc)] for l in text)
