import cv2
import numpy as np
import matplotlib.pyplot as plt
imagen = cv2.imread('C:/Users/VTOLW/OneDrive/Pictures/elena.png') # Cargamos una imagen
#Convierte la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
def calcular_luminancia (x, y): # Función para calcular la luminancia en un punto especifico
    return imagen_gris [y, x]
# Coordenadas de un punto específico
x_punto = 100
y_punto = 150
#Muestra la luminancia del punto específico
luminancia_punto = calcular_luminancia (x_punto, y_punto)
print(f"Luminancia en ({x_punto}, {y_punto}): {luminancia_punto}")
def obtener_puntos_vecinos (x, y, radio=1): # Define una función para obtener los valores de los puntos vecinos
    puntos_vecinos = []
    for i in range(-radio, radio + 1):
        for j in range(-radio, radio + 1):
            if 0 <= x + i < imagen_gris.shape[1] and 0 <= y + j < imagen_gris.shape[0]:
                puntos_vecinos.append((x + i, y + j))
        return puntos_vecinos
#Coordenadas de los puntos vecinos del punto específico
radio_vecinos = 1
puntos_vecinos = obtener_puntos_vecinos(x_punto, y_punto, radio_vecinos)

for x, y in puntos_vecinos: #Muestra la luminancia de los puntos vecinos
    luminancia_vecino = calcular_luminancia (x, y)
    print(f"Luminancia en ((x), {y}): {luminancia_vecino}")
#Dibuja círculos en los puntos específicos y sus vecinos en la imagen
imagen_con_resaltados = imagen.copy()
for x, y in puntos_vecinos + [(x_punto, y_punto)]:
    cv2.circle(imagen_con_resaltados, (x, y), 5, (0, 255, 0), -1) # Resaltado en verde
#Muestra la imagen con los resaltados
plt.imshow(cv2.cvtColor(imagen_con_resaltados, cv2.COLOR_BGR2RGB))
plt.title('Imagen con resaltados')
plt.axis('off') # Oculta ejes
plt.show()