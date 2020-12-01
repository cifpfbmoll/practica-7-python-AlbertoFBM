# PRÁCTICA 7 --> EJERCICIO 1
# Escribe un programa que pida un texto por pantalla, este texto lo pase
# como parámetro a un procedimiento, y éste lo imprima primero todo en
# minúsculas y luego todo en mayúsculas.
import os
os.system("cls")

def mayusMinus (sentence):

    minus = sentence.lower()
    print("En minúsculas:")
    print('-->', minus)

    mayus = sentence.upper()
    print("En mayúsculas: ")
    print('-->', mayus)



sentence = input("Pon una frase: ")

mayusMinus(sentence)







