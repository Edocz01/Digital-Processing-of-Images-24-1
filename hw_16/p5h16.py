import cv2
imagen = cv2.imread('C:/Users/VTOLW/OneDrive/Pictures/elena.png')
nueva_altura = 300
nueva_anchura = 400
imagen_redimensionada = cv2.resize(imagen, (nueva_anchura, nueva_altura))
cv2.imwrite('imagen_redimensionada.jpg', imagen_redimensionada)
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Redimensionada', imagen_redimensionada)
cv2.waitKey(0)
cv2.destroyAllWindows()