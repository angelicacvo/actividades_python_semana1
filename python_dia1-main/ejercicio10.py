numero = int(input("Ingresa un número: "))

def funcion_rango():
    if numero in range(1, 11):
        print("Está dentro del rango de 1-10")
    else:
        print("No está dentro del rango")

funcion_rango()
