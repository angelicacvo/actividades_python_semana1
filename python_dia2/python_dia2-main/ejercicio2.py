numeros = [1, 3, 5 ,7 ,9]
numero_usuario = int(input("Ingresa un número "))

def verificar_numero():
    if numero_usuario in numeros:
        print(f"El número {numero_usuario} está en la lista")
    else:
        print(f"El número {numero_usuario} no está en la lista")

verificar_numero()