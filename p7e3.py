# PRÁCTICA 7 --> EJERCICIO 3
# Escribe un programa que lea (entrada por teclado) una frase, y la pase
# como parámetro a un procedimiento, y éste debe mostrar la frase con
# un carácter en cada línea.
import os
os.system("cls")

def ponerFrase(frase):
    for i in range(len(frase)):
        print(frase[i])

frase = input("Pon una frase: ")

ponerFrase(frase)