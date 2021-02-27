"""
Inserta el encabezado aquí y escribe tu código abajo


# Declaraciones
CONSTANTE = valor

# Entradas
entrada = input()

# Proceso


# Salidas
print(salida)
"""
"""
Comienza con A
"""

# Entradas
palabra = input("Escriba una palabra: ")

# Proceso
if len(palabra) > 0 and palabra[0].lower() in "aá":
    comienza = "comienza"
else:
    comienza = "no comienza"
respuesta = "'" + palabra + "' " + comienza + " con 'A'"

# Salidas
print(respuesta)
