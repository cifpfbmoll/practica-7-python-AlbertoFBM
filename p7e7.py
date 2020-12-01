# PRÁCTICA 7 --> EJERCICIO 7
# Escribe un programa que lea una frase (entrada por teclado),
# y la pase como parámetro a un procedimiento. El procedimiento 
# contará el número de vocales (de cada una) que aparecen, y lo 
# imprimirá por pantalla.
import os
os.system("cls")

def contarVocales(frase):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for k in range(len(frase)):
        if(frase[k] == "a"):
            a += 1
        if(frase[k] == "e"):
            e += 1
        if(frase[k] == "i"):
            i += 1
        if(frase[k] == "o"):
            o += 1
        if(frase[k] == "u"):
            u += 1
    return print("a =", a," e =", e, " i =", i," o =", o, " u =", u)

frase = input("Escribe una frase: ")

contarVocales(frase)