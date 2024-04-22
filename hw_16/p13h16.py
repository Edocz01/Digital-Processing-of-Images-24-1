import cv2
#Cargar la imagen
imagen = cv2.imread('C:/Users/VTOLW/OneDrive/Pictures/bob_cholo_png.png')
#Escalar la imagen a un tamaño específico
nuevo_ancho = 400
nuevo_alto = 300
imagen_escalada = cv2.resize(imagen, (nuevo_ancho, nuevo_alto))
# Mostrar la imagen escalada
cv2.imshow('Imagen Escalada', imagen_escalada)
#Hacer zoom en la imagen
factor_de_zoom = 2 # Ajusta este valor según lo que desees
imagen_zoom = cv2.resize(imagen, (imagen.shape[1] * factor_de_zoom, imagen.shape[0] * factor_de_zoom))
# Mostrar la imagen con zoom
cv2.imshow('Imagen con Zoom', imagen_zoom)
cv2.waitKey(0)
# Liberar los recursos y cerrar la ventana
cv2.destroyAllWindows()