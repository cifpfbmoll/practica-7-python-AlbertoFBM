# PRÁCTICA 7 --> EJERCICIO 12
# Escribir un programa que lea una frase, y pase ésta como parámetro 
# a una función que debe contar el número de palabras que contiene. 
# Debe imprimir el programa principal el resultado. Asumir que cada 
# palabra está separada por un solo blanco:
# a) Asumir que cada palabra está separada por un solo blanco.
# b) No se sabe cómo están separadas las palabras. Pueden estar separadas
# por más de un blanco o por signos de puntuación.

import os
os.system("cls")

def contarPalabras(frase):
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p',"q","r","s","t","u","v","w","x","y","z"]
    signos = [',','.',':',';','-']
    palabras = 0
    for i in range(len(frase)):
        if (frase[i] == " " and (frase[i-1] in signos or frase[i-1] in letras)):
            palabras += 1
    if (len(frase) != 0):
        palabras += 1

    return print(f"La frase <<{frase}>> tiene {palabras} palabras.")



frase = input("Escribe una frase: ")
contarPalabras(frase)