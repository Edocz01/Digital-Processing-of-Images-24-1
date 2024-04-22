import cv2
import numpy as np
imagen = cv2.imread('C:/Users/VTOLW/OneDrive/Pictures/elena.png')
M = np.array([[2, 0, 0], [0, 0.5, 0]], dtype=float)
deformada = cv2.warpAffine (imagen, M, (imagen.shape[1], imagen.shape[0]))
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Deformada', deformada)
cv2.waitKey(0)
cv2.destroyAllWindows()