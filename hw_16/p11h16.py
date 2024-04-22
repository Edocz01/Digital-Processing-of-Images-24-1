import cv2 
import numpy as np
#Cargar dos imágenes de entrada
image1 = cv2.imread('C:/Users/VTOLW/OneDrive/Pictures/elena.png')
image2 = cv2.imread('C:/Users/VTOLW/OneDrive/Pictures/bob_cholo_png.png')
# Asegurarse de que ambas imágenes tengan el mismo tamaño
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
# Parámetro para la transición entre imágenes (0.0 a 1.0)
alpha = 0.5
#Realizar la transformación de fundido entre las dos imágenes
blended = cv2.addWeighted(image1, alpha, image2, 1 - alpha, 0)
#Realizar la transformación de hinchado (scale)
scale_factor = 1.5
hinchado = cv2.resize(image1, (image1.shape[1], image1.shape[0]))# Redimensionar para que tenga el mismo tamaño que image1
#Realizar morphing entre las dos imágenes 
morphed = cv2.addWeighted(image1, alpha, hinchado, 1 - alpha, 0)
# Mostrar las imágenes originales, el fundido, el hinchado y el morphing
cv2.imshow('Imagen 1', image1)
cv2.imshow('Imagen 2', image2) 
cv2.imshow('Fundido', blended)
cv2.imshow('Hinchado', hinchado)
cv2.imshow('Morphing', morphed)

#Esperar a que el usuario presione una tecla y luego cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()