import cv2
import numpy as np
image = cv2.imread("C:/Users/VTOLW/OneDrive/Pictures/elena.png")
scale_factor = 2
imagen_escalada = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)
x_translation = 50
y_translation = 30
translation_matrix = np.float32([[1, 0, x_translation], [0, 1, y_translation]])
imagen_traducida = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
angle = 45 
rotation_matrix = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), angle, 1)
imagen_rotada = cv2.warpAffine (image, rotation_matrix, (image.shape[1], image.shape[0]))
espejo_horizontal = cv2.flip(image, 1)
espejo_vertical = cv2.flip(image, 0)
ambos_espejo = cv2.flip(image, -1)
cv2.imshow('Imagen escalada', imagen_escalada)
cv2.imshow('Imagen traducida', imagen_traducida)
cv2.imshow('Imagen rotada', imagen_rotada)
cv2.imshow('Espejo horizontal', espejo_horizontal)
cv2.imshow('Espejo vertical', espejo_vertical)
cv2.imshow('Ambos espejos', ambos_espejo)
cv2.waitKey(0)
cv2.destroyAllWindows()