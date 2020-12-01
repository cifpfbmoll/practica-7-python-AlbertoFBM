# PRÁCTICA 7 --> EJERCICIO 2
# Escribe un programa que lea (entrada por teclado) el nombre y
# los dos apellidos de una persona (en tres cadenas de caracteres
# diferentes), los pase como parámetros a una función, y ésta debe
# unirlos y devolver una única cadena. La cadena final la imprimirá
# el programa por pantalla.
import os
os.system("cls")

def ponerNombre(complete_name):
    n = name + ' '  + surname1 + ' ' + surname2
    print("Tu nombre es:", n)

name = input("Pon tu nombre: ")
surname1 = input("Pon tu primer apellido: ")
surname2 = input("Pon tu segundo apellido: ")

complete_name = name + surname1 + surname2

ponerNombre(complete_name)
