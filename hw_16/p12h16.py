mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_lista = mi_lista [2:5] # Obtiene elementos desde el índice 2 al 4 (5 no incluido)
primeros_tres = mi_lista[:3] # Obtiene los primeros 3 elementos
ultimos_tres = mi_lista[6:] # obtiene los últimos 3 elementos

print("Slicing en lista:")
print("sub_lista:", sub_lista) # Output: [3, 4, 5]
print("primeros_tres:", primeros_tres) # Output: [1, 2, 3]
print("ultimos_tres:", ultimos_tres) # Output: [7, 8, 9]

# Slicing en una cadena
mi_cadena = "Hola, mundo"
sub_cadena = mi_cadena [0:4] # Obtiene "Hola"
ultimos_cinco = mi_cadena[-5:] # Obtiene "mundo"

print("\nSlicing en cadena:")
print("sub_cadena:", sub_cadena) # Output: Hola
print("ultimos_cinco:", ultimos_cinco) # Output: mundo

# Slicing en una tupla
mi_tupla = (10, 20, 30, 40, 50)
sub_tupla = mi_tupla [1:4] # Obtiene (20, 30, 40)

print("\nslicing en tupla:")
print("sub_tupla:", sub_tupla) # Output: (20, 30, 40)