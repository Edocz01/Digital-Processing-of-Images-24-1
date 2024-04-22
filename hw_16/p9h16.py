from PIL import Image
imagen_original = Image.open('C:/Users/VTOLW/OneDrive/Pictures/elena.png')
ancho, alto = imagen_original.size
imagen_espejo = Image.new("RGB", (ancho * 2, alto))
imagen_espejo.paste(imagen_original, (0, 0))
imagen_invertida = imagen_original.transpose (Image. FLIP_LEFT_RIGHT)
imagen_espejo.paste(imagen_invertida, (ancho, 0))
imagen_espejo.save("imagen_espejo.jpg")
imagen_espejo.show()
