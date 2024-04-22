import cv2
# Cargar la imagen
imagen = cv2.imread('C:/Users/VTOLW/OneDrive/Pictures/bob_cholo.jpg')
# Definir la nueva resolución deseada
nueva_altura = 300
nueva_anchura = 400
# Redimensionar la imagen a la nueva resolución
imagen_redimensionada = cv2.resize(imagen, (nueva_anchura, nueva_altura))
# Guardar la imagen redimensionada
cv2.imwrite('imagen_redimensionada.jpg', imagen_redimensionada)
# Mostrar la imagen original y la redimensionada
cv2.imshow('Imagen Original', imagen) 
cv2.imshow('Imagen Redimensionada', imagen_redimensionada)
# Esperar a que el usuario presione una tecla y luego cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()