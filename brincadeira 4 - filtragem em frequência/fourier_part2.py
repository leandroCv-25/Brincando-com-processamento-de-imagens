
import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt,exp

def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def idealFilterLP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            if distance((y,x),center) < D0*rows:
                base[y,x] = 1
    return base


def butterworthLP(D0,imgShape,n):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1/(1+(distance((y,x),center)/(D0*rows))**(2*n))
    return base

def gaussianLP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = exp(((-distance((y,x),center)**2)/(2*((D0*rows)**2))))
    return base



plt.figure(figsize=(8*3, 6*3), constrained_layout=False)

D0 = 0.5

img = cv2.imread("images/lena.jpg", 0)
img1 = np.fft.fft2(img)
img2 = np.fft.fftshift(img1)

lowPassIdeal = idealFilterLP(D0,img.shape)

img3 = img2*lowPassIdeal
img4 = np.fft.ifftshift(img3)
img5 = np.fft.ifft2(img3)

plt.subplot(1,3,1), plt.imshow(img, "gray"), plt.title("Imagem Original")
plt.subplot(1,3,2), plt.imshow(np.log(1+np.abs(lowPassIdeal)), "gray"), plt.title("Filtro Passa baixa ideal D0 = "+str(D0))
plt.subplot(1,3,3), plt.imshow(np.abs(img5), "gray"), plt.title("Imagem Resultante")

plt.show()

lowPassButterworth = butterworthLP(D0,img.shape,3)

img3 = img2*lowPassButterworth
img4 = np.fft.ifftshift(img3)
img5 = np.fft.ifft2(img3)

plt.subplot(1,3,1), plt.imshow(img, "gray"), plt.title("Imagem Original")
plt.subplot(1,3,2), plt.imshow(np.log(1+np.abs(lowPassButterworth)), "gray"), plt.title("Filtro Passa baixa Butterworth D0 = "+str(D0))
plt.subplot(1,3,3), plt.imshow(np.abs(img5), "gray"), plt.title("Imagem Resultante")

plt.show()

lowPassGaussian = gaussianLP(D0,img.shape)

img3 = img2*lowPassGaussian
img4 = np.fft.ifftshift(img3)
img5 = np.fft.ifft2(img3)

plt.subplot(1,3,1), plt.imshow(img, "gray"), plt.title("Imagem Original")
plt.subplot(1,3,2), plt.imshow(np.log(1+np.abs(lowPassGaussian)), "gray"), plt.title("Filtro Passa baixa Gaussian D0 = "+str(D0))
plt.subplot(1,3,3), plt.imshow(np.abs(img5), "gray"), plt.title("Imagem Resultante")

plt.show()