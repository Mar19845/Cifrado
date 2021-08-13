
import numpy as np
import matplotlib.pyplot as plt
import re
from skimage import io,data  
from PIL import Image  
#import los algoritmos que generan cadenas de bits
import lcg as lcg
import lfsr as lfsr
import WichmanHill as Wichman_Hill

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
    bit=''
    for i in range(0, m):
        for j in range(0, n):
            #print(str(bin(I[i,j]))[2:])
            c=str(bin(I[i,j]))[2:]
            c=c.replace('b','')
            bit+= c
    return bit

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

def init_compare_data():

    img = io.imread('mono2.png',as_gray=True)

    J = Image.fromarray(img)
    J = J.resize((J.size[0]//2, J.size[1]//2), Image.LANCZOS)
    I = np.array(J) * 255
    I = I.astype(int)


    plt.figure()
    plt.imshow(I, cmap='gray')
    plt.suptitle('Imagen Original')
    plt.show()

    #cadena de la imagen original y las cadena aleatoria
    bit_img= img2bits(I)
    bit_lcg = lcg.init_lcg(len(bit_img))
    bit_wh = Wichman_Hill.Wichmann_Hill(len(bit_img))
    bit_lfsr = lfsr.lfsr(len(bit_img), [4, 2, 5], 6)

    #xor de la cadena de la imagen original y las cadena aleatoria
    xor_img_lcg = xor(bit_img,bit_lcg)
    xor_img_wh = xor(bit_img,bit_wh)
    xor_img_lfsr= xor(bit_img,bit_lfsr)

    I_lcg = bits2img(bit_lcg, I.shape)
    I_xor_lcg = bits2img(xor_img_lcg, I.shape)
    I_og_after_xor_lcg = bits2img(xor(bit_lcg,xor_img_lcg), I.shape)
    #lcg
    plt.figure(figsize=(15,8))
    plt.subplot(1,2,1)
    plt.imshow(I_lcg, cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(I_xor_lcg, cmap='gray')
    plt.suptitle('Imagenes de bits de LCG vs XOR con imagen original')
    plt.show()
    plt.figure(figsize=(15,8))
    plt.subplot(1,2,1)
    plt.imshow(I, cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(I-I_xor_lcg, cmap='gray')
    plt.suptitle('Imagen original vs Resta de las imagenes de bits de LCG')
    plt.show()
    
    I_wh = bits2img(bit_wh, I.shape)
    I_xor_wh = bits2img(xor_img_wh, I.shape)
    I_og_after_xor_wh = bits2img(xor(bit_wh,xor_img_wh), I.shape)
    #william 
    plt.figure(figsize=(15,8))
    plt.subplot(1,2,1)
    plt.imshow(I_wh, cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(I_xor_wh, cmap='gray')
    plt.suptitle('Imagenes de bits de WH vs XOR con imagen original')
    plt.show()
    plt.figure(figsize=(15,8))
    plt.subplot(1,2,1)
    plt.imshow(I, cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(I_wh-I_xor_wh, cmap='gray')
    plt.suptitle('Imagen original vs Resta de las imagenes de bits de WH')
    plt.show()

    I_lfsr = bits2img(bit_lfsr, I.shape)
    I_xor_lfsr = bits2img(xor_img_lfsr, I.shape)
    I_og_after_xor_wh = bits2img(xor(bit_wh,xor_img_wh), I.shape)
    #lfsr 
    plt.figure(figsize=(15,8))
    plt.subplot(1,2,1)
    plt.imshow(I_lfsr, cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(I_xor_lfsr, cmap='gray')
    plt.suptitle('Imagenes de bits de LFSR vs XOR con imagen original')
    plt.show()
    plt.figure(figsize=(15,8))
    plt.subplot(1,2,1)
    plt.imshow(I, cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(I_lfsr-I_xor_lfsr, cmap='gray')
    plt.suptitle('Imagen original vs Resta de las imagenes de bits de LFSR')
    plt.show()