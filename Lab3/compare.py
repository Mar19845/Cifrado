
import numpy as np
import matplotlib.pyplot as plt
import re
from skimage import io,data  
from PIL import Image  


img = io.imread('image.jpg',as_gray=True)

J = Image.fromarray(img)
J = J.resize((J.size[0]//2, J.size[1]//2), Image.LANCZOS)
I = np.array(J)
plt.figure()
plt.imshow(I, cmap='gray')
plt.show()

def xor(a, b):
    m = len(a)
    n = len(b)
    maxx = max(m,n)
    if (m < n):
        a = a + (n-m)*'0'
    if (n < m):
        b = b + (m-n)*'0'
        
    c = ''
    for i in range(0, maxx):
        c = c + str(int(a[i]) ^ int(b[i]))
    return c

def img2bits(I):
    ''' Convierte una imagen en escala de grises a cadena de bits.
        Input:  I = imagen, como numpy array de shape (m,n).
        Output: s = string de bits, donde se concatenan cada pixel de I.
    '''
    m, n = I.shape
    s = ''
    for i in range(0, m):
        for j in range(0, n):
            s = s + '{0:08b}'.format(I[i,j])
    return s

def bits2img(x, shape):
    ''' Convierte una cadena de bits a una imagen en escala de grises.
        Input:  s = string de bits, donde se concatenan cada pixel de I.
                shape = dimensiones (m,n) de la imagen de salida I.
        Output: I = imagen, como numpy array de shape (m,n).
    '''

    m, n = shape
    I = np.zeros(m*n).astype(np.uint8)
    bts = re.findall('........', x)
    for i in range(0, len(bts)):
        I[i] = int(bts[i], 2)
    I = I.reshape(m,n)
    return I