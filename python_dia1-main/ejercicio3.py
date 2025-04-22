numero = float(input("Ingresa un número: "))

def verificar_numero():
    if numero % 2 == 0:
        print("EL número es par")
    else:
        print("El número es impar")

verificar_numero()