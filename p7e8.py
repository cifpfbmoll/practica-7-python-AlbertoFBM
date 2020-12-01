# PRÁCTICA 7 --> EJERCICIO 8
# Escribe un programa que pida una frase (entrada por teclado), y pase 
# la frase como parámetro a una función que debe eliminar los espacios 
# en blanco (compactar la frase). El programa principal imprimirá por 
# pantalla el resultado final.

import os
os.system("cls")

def quitarEspacios(frase):
    for i in range(len(frase)):
        if (frase[i] == " "):
            nuevafrase = frase.replace(frase[i],"")
    return print(nuevafrase)


frase = input("Escribe una frase: ")

quitarEspacios(frase)