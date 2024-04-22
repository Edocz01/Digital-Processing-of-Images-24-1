import cv2
imagen = cv2.imread('C:/Users/VTOLW/OneDrive/Pictures/elena.png')
nuevo_ancho = 400
nuevo_alto = 300
imagen_escalada = cv2.resize(imagen, (nuevo_ancho, nuevo_alto))
cv2.imshow('Imagen Escalada', imagen_escalada)
factor_de_zoom = 2 # Ajusta este valor según lo que desees
imagen_zoom = cv2.resize(imagen, (imagen.shape[1] * factor_de_zoom, imagen.shape[0] * factor_de_zoom))
cv2.imshow('Imagen con Zoom', imagen_zoom)
cv2.waitKey(0)
cv2.destroyAllWindows()