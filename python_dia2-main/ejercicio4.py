edad = int(input("Ingresa tu edad "))

def validar_edad():
    if edad < 0 or edad > 120:
        print("Edad no válida")
    else:
        print("Edad válida")

validar_edad()