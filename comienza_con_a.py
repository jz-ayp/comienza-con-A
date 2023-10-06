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
