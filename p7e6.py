# PRÁCTICA 7 --> EJERCICIO 6
# Escribe un programa que lea el nombre de una persona y un carácter
# (entrada por teclado), le pase estos datos a una función que comprobará
# si dicho carácter está en su nombre. El resultado de dicha función lo 
# imprimirá el programa principal por pantalla.
import os
os.system("cls")

def nombreCaracter(nombre, caracter):
    for i in range(len(nombre)):
        if (nombre[i] == caracter):
            return nombreCaracter
        else:
            print(f"El carácter {caracter} no está en el nombre {nombre}")
nombre = input("Dime un nombre: ")
caracter = input("Dime un carácter: ")
nombreCaracter(nombre, caracter)
print(f"El carácter {caracter} está en el nombre {nombre}.")
