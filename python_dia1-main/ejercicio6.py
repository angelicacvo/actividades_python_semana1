from random import *

numero_secreto = randint(0, 10)
numero_usuario = int(input("Ingresa un número: "))

def adivinar_numero(): 
    if numero_usuario > numero_secreto:
        print("Tu número es mayor al número sorpresa")
    elif numero_usuario < numero_secreto: 
        print("Tu número es menor al número sorpresa")
    else: 
        print("Este es el número sorpresa")

adivinar_numero()