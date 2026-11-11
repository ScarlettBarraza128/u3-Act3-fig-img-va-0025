import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt

print("Emily Barraza NC = 0025")
print("UIII Act3 colocar puntos a una imagen en blanco y negro VA")
img_tyle = cv2.imread("tyler the creator.png")
plt.imshow(img_tyle)
plt.title("tyler the creator y Emily Barraza 0025")
plt.show()

print("-+-+-+-+-+-+-+ puntos en la imagen +-+-+-+-+-+-+-+-+-")
plt.imshow(img_tyle)
x = [100, 150, 200]
y = [100, 150, 200]
plt.scatter(x, y, s=20, c="red")
plt.title("tyler the creator y Emily Barraza 0025")
plt.show()
print("-+-+-+-+-+-+-+ cuadro en la imagen +-+-+-+-+-+-+-+-+-")
img_tyler = cv2.imread("tyler the creator.png")
plt.imshow(img_tyle)
x = [80, 240, 240, 80, 80]
y = [40, 40, 200, 200, 40]
plt.plot(x,y,c="blue")
plt.title("tyler the creator y Emily Barraza 0025")
plt.show()
print("-+-+-+-+-+-+-+ circulo verde en la imagen +-+-+-+-+-+-+-+-+-")
plt.imshow(img_tyler)
N = 30 # lados del polígono / circulo
x = np.zeros((N+1,))
y = np.zeros((N+1,))

# Centro (xc, yc) y radio (r) basados en las dimensiones del cuadro azul
(xc, yc) = (160, 120) 
r = 80
for k in range(N+1):
    t = 2 * np.pi / N * k
    x[k] = xc + r * np.cos(t)
    y[k] = yc + r * np.sin(t)
plt.plot(x, y, c="green")
plt.title("tyler the creator y Emily Barraza 0025")
plt.show()