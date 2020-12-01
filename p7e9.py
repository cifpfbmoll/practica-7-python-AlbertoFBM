# PRÁCTICA 7 --> EJERCICIO 9
# Escribe un programa que pida dos palabras las pase como parámetro 
# a un procedimiento y diga si riman o no. Si coinciden las tres últimas 
# letras tiene que decir que riman. Si coinciden solo las dos últimas 
# tiene que decir que riman un poco y si no, que no riman.

import os
os.system("cls")

def buenasRimas(palabra1, palabra2):
        if(palabra1[-3:] == palabra2[-3:]):
            print(f"Las palabras {palabra1} y {palabra2} riman !!!")
        elif(palabra1[-2:] == palabra2[-2:]):
            print(f"Las palabras {palabra1} y {palabra2} riman un poquito.")
        else:
            print(f"Las palabras {palabra1} y {palabra2} no riman nada...")


print("Pon dos palabras y te diré si riman.")
palabra1 = input("Pon la primera palabra: ")
palabra2 = input("Pon la segunda palabra: ")

buenasRimas(palabra1, palabra2)