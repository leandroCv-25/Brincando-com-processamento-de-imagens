import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

img_c1 = cv2.imread("images/img.jpg", 0)
img_c2 = np.fft.fft2(img_c1)
img_c3 = np.fft.fftshift(img_c2)

ponto = (512 / 2, 512 / 2) #ponto no centro da figura
rotacao = cv2.getRotationMatrix2D(ponto, 40, 1.0)
img_r1 = cv2.warpAffine(img_c1, rotacao, (512, 512))
img_r2 = np.fft.fft2(img_r1)
img_r3 = np.fft.fftshift(img_r2)

deslocamento = np.float32([[1, 0, 50], [0, 1, 50]])
img_t1 = cv2.warpAffine(img_c1, deslocamento, (512, 512))
img_t2 = np.fft.fft2(img_t1)
img_t3 = np.fft.fftshift(img_t2)

plt.subplot(1,5,1), plt.imshow(img_c1, "gray"), plt.title("Image Original")
plt.subplot(1,5,2), plt.imshow(np.log(1+np.abs(img_c2)), "gray"), plt.title("Spectrum")
plt.subplot(1,5,3), plt.imshow(np.angle(img_c2), "gray"), plt.title("Phase")
plt.subplot(1,5,4), plt.imshow(np.log(1+np.abs(img_c3)), "gray"), plt.title("Spectrum Centralizado")
plt.subplot(1,5,5), plt.imshow(np.angle(img_c3), "gray"), plt.title("Phase Centralizada")

plt.show()

plt.subplot(1,5,1), plt.imshow(img_r1, "gray"), plt.title("Image Rotacionada")
plt.subplot(1,5,2), plt.imshow(np.log(1+np.abs(img_r2)), "gray"), plt.title("Spectrum")
plt.subplot(1,5,3), plt.imshow(np.angle(img_r2), "gray"), plt.title("Phase")
plt.subplot(1,5,4), plt.imshow(np.log(1+np.abs(img_r3)), "gray"), plt.title("Spectrum Centralizado")
plt.subplot(1,5,5), plt.imshow(np.angle(img_r3), "gray"), plt.title("Phase Centralizada")
plt.show()

plt.subplot(1,5,1), plt.imshow(img_t1, "gray"), plt.title("Image Deslocada")
plt.subplot(1,5,2), plt.imshow(np.log(1+np.abs(img_t2)), "gray"), plt.title("Spectrum")
plt.subplot(1,5,3), plt.imshow(np.angle(img_t2), "gray"), plt.title("Phase")
plt.subplot(1,5,4), plt.imshow(np.log(1+np.abs(img_t3)), "gray"), plt.title("Spectrum Centralizado")
plt.subplot(1,5,5), plt.imshow(np.angle(img_t3), "gray"), plt.title("Phase Centralizada")
plt.show()