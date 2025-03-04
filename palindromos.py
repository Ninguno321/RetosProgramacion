'''
Reto: Crea un programa en Python que pida al usuario que ingrese una cadena de texto 
y determine si es un palíndromo. Un palíndromo es una palabra o frase que se lee igual 
hacia adelante y hacia atrás, ignorando espacios, mayúsculas y signos de puntuación. 
El programa debe imprimir un mensaje indicando si la cadena es un palíndromo o no.
'''

import string


def esPalindromo(cadena):
    #Lo primero que haremos sera quitar los espacios y los signos de puntuacion
    cadena = ''.join(c for c in cadena if c.isalnum()).lower()
    #Ahora la invertimos para comparar
    cadenaInvertida = cadena[::-1]
    return cadena == cadenaInvertida
    
def main():
    cadena_de_entrada = input("Ingrese una cadena de texto: ")
    if esPalindromo(cadena_de_entrada):
        print(f"La cadena '{cadena_de_entrada}' es un palíndromo")
    else: 
        print(f"La cadena '{cadena_de_entrada}' no es un palíndromo")
main()