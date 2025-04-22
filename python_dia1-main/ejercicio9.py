ano = int(input("Ingresa un año "))

def calcular_bisiesto():
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("Año bisiesto")
    else:
        print("No es un año bisiesto")

calcular_bisiesto()