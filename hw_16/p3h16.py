import cv2
import numpy as np
imagen = cv2.imread('C:/Users/VTOLW/OneDrive/Pictures/elena.png')
angulo_rotacion = 45
altura, ancho = imagen.shape[:2]
centro = (ancho // 2, altura // 2)
matriz_rotacion = cv2.getRotationMatrix2D (centro, angulo_rotacion, 1.0)
imagen_rotada = cv2.warpAffine (imagen, matriz_rotacion, (ancho, altura))
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Rotada', imagen_rotada)
cv2.waitKey(0)
cv2.destroyAllWindows()