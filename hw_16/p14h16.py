import cv2
import numpy as np
# Cargamos la imagen
imagen = cv2.imread('C:/Users/VTOLW/OneDrive/Pictures/bob_cholo.jpg')
# Definimos la cantidad de desplazamiento en píxeles
desplazamiento_x = 50 # Desplazamiento horizontal
desplazamiento_y = 30 # Desplazamiento vertical
# Obtenemos las dimensiones de la imagen
alto, ancho = imagen.shape[:2]
# Creamos la matriz de transformación para la translación
matriz_translacion = np.float32([[1, 0, desplazamiento_x], [0, 1, desplazamiento_y]])
# Aplicamos la translación a la imagen utilizando warpAffine
imagen_transladada = cv2.warpAffine(imagen, matriz_translacion, (ancho, alto))
# Mostramos la imagen original y la imagen transladada
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Transladada', imagen_transladada)
cv2.waitKey(0)
cv2.destroyAllWindows()