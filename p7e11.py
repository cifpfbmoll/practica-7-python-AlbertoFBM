# PRÁCTICA 7 --> EJERCICIO 11
# Escribe un programa que te pida una frase, y pase la frase como
# parámetro a una función. Ésta debe devolver si es palíndroma o no, 
# y el programa principal escribirá el resultado por pantalla:
import os
os.system("cls")

def esPalindroma(frase):
    igual = 0
    auxiliar = 0
    for i in reversed(range(len(frase))):
        if frase[i].lower() == frase[auxiliar].lower():
            igual += 1
        auxiliar += 1
    if len(frase) == igual:
        print("<<", frase, ">>", "és palíndroma.")
    else:
        print("La frase <<", frase, ">>", "NO és palíndroma.")

frase = input("Dime una frase y te diré si es palíndroma o no: ")
esPalindroma(frase)