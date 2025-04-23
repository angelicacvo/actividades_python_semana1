numero1 = int(input("Ingresa el primer número "))
numero2 = int(input("Ingresa el segundo número "))
numero3 = int(input("Ingresa el tercer número "))

def comprobar_numero():
    if numero1 < numero2 and numero1 < numero3:
        print(f'El número menor es el primer número: {numero1}')
    elif numero2 < numero1 and numero2 < numero3:
        print(f'El número menor es el segundo número: {numero2}')
    elif numero3 < numero1 and numero3 < numero2:
        print(f'El número menor es el tercer número {numero3}')

comprobar_numero()

