import pygame
import sys
# Inicializa Pygame
pygame.init()
# Dimensiones de la ventana de visualización
window_width = 400
window_height = 400
# Crear la ventana de visualización
window = pygame.display.set_mode((window_width, window_height))
#Color de fondo
background_color= (255, 255, 255)
#color del rectángulo
rectangle_color= (255, 0, 0)
# Coordenadas y tamaño del rectángulo
rectangle_x = 100
rectangle_y = 100
rectangle_width = 200
rectangle_height = 200
# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Borrar la ventana
    window.fill(background_color)
    # Dibujar el rectángulo
    pygame.draw.rect(window, rectangle_color, (rectangle_x, rectangle_y, rectangle_width, rectangle_height))
    # Realizar el "clipping" para que el rectángulo esté dentro de la ventana
    #Esto asegura que el rectángulo no se dibuje fuera de la ventana de visualización
    #Limitar el lado izquierdo del rectángulo
    if rectangle_x < 0:
        rectangle_x = 0
    #Limitar el lado derecho del rectángulo
    if rectangle_x + rectangle_width > window_width:
        rectangle_x = window_width - rectangle_width
    #Limitar la parte superior del rectángulo
    # Limitar la parte superior del rectángulo
    if rectangle_y < 0:
        rectangle_y = 0
    # Limitar la parte inferior del rectángulo
    if rectangle_y + rectangle_height > window_height:
        rectangle_y = window_height - rectangle_height
    # Actualizar la ventana
    pygame.display.flip()
# Salir de Pygame
pygame.quit()
sys.exit()