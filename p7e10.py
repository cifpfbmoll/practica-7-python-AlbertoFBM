# PRÁCTICA 7 --> EJERCICIO 10
# Escribe un programa que te pida una palabra o número, pase por 
# parámetro estos datos a una función, y ésta te diga si es o no 
# palíndroma o capicúa. El programa principal imprimirá el resultado 
# de la función:

import os
os.system("cls")

def esCapi(num_pal):
    igual = 0
    auxiliar = 0
    for i in reversed(range(len(num_pal))):
        if num_pal[i].lower() == num_pal[auxiliar].lower():
            igual += 1
        auxiliar += 1
    if len(num_pal) == igual:
        print("<<", num_pal, ">>", "es palíndroma o capicúa")
    else:
        print("<<", num_pal, ">>", "NO es palíndroma o capicúa")

print("Pon un número o una palabra y te diré si es capicúa, palíndroma o nada")
num_pal = input("Pon un número o una frase: ")
esCapi(num_pal)
