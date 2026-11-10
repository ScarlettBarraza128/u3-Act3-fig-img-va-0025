import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt

print("Emily Barraza NC = 0025")
print("UIII Act3 colocar puntos a una imagen en blanco y negro VA")
mi_imagen = cv2.imread("tyler the creator.png")
plt.imshow(mi_imagen)
plt.title("tyler the creator y Emily Barraza 0025")
plt.show()

print("-+-+-+-+-+-+-+ puntos en la imagen +-+-+-+-+-+-+-+-+-")
plt.imshow(mi_imagen)
x = [100, 150, 200]
y = [100, 150, 200]
plt.scatter(x, y, s=20, c="red")
plt.show()

