# PRÁCTICA 7 --> EJERCICIO 5
# Escribe un programa que te pida una frase y una vocal (entrada por teclado),
# y pase estos datos como parámetro a una función que se encargará de cambiar 
# todas las vocales de la frase por la vocal seleccionada. Devolverá la función 
# la frase modificada, y el programa principal la imprimirá:

import os
os.system("cls")

lista = ["a","e","i","o","u"]
def cambiarVocal(frase,vocal):
    for i in range(len(frase)):
        if frase[i] in lista:
            frase = frase[:i] + vocal + frase[(i+1):] 
    return frase

print("Dime una frase y una vocal")
frase = input("Dime la frase: ")
vocal = input("Dime una vocal: ")

cambiarVocal(frase,vocal)

print(cambiarVocal(frase,vocal))