import cv2
imagen = cv2.imread('C:/Users/VTOLW/OneDrive/Pictures/elena.png', 0)
umbral = 128 
_, imagen_binarizada = cv2.threshold (imagen, umbral, 255, cv2.THRESH_BINARY)
cv2.imshow('Imagen Original', imagen) 
cv2.imshow('Imagen Binarizada', imagen_binarizada)
cv2.waitKey(0) 
cv2.destroyAllWindows()