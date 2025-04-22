peso = float(input("Ingresa tu peso "))
altura = float(input("ingresa tu altura "))

def calcular_imc():
    imc = float(peso/(altura**2))
    if imc < 18.5:
        print("Bajo peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Peso normal")
    elif imc >= 25 and imc <= 29.9:
        print("Sobrepeso")
    elif imc >= 30: 
        print("Obesidad")

calcular_imc()
