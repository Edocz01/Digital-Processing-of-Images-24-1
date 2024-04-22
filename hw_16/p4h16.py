import cv2
import numpy as np
imagen = cv2.imread('C:/Users/VTOLW/OneDrive/Pictures/elena.png')
desplazamiento_x = 50
desplazamiento_y = 30
alto, ancho = imagen.shape[:2]
matriz_translacion = np.float32([[1, 0, desplazamiento_x], [0, 1, desplazamiento_y]])
imagen_transladada = cv2.warpAffine(imagen, matriz_translacion, (ancho, alto))
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Transladada', imagen_transladada)
cv2.waitKey(0)
cv2.destroyAllWindows()
