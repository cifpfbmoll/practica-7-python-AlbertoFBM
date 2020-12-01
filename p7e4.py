# PRÁCTICA 7 --> EJERCICIO 4
# Escribe un programa que pida una frase (entrada por teclado),
# y le pase como parámetro a una función dicha frase. La función
# debe sustituir todos los espacios en blanco de una frase por un asterisco,
# y devolver el resultado para que el programa principal la imprima por pantalla.
import os
os.system("cls")

def ponerAsterisco (frase):
    for i in range(len(frase)):
        if frase[i] == " ":
            frase = frase[:i] +"*"+ frase[(i+1):]
    return frase

frase = input("Ponga una frase: ")

ponerAsterisco (frase)
print(ponerAsterisco(frase))