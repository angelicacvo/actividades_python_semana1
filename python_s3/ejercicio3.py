def verify(number):
    if number % 2 == 0:
        return f"{number} es un número par."
    else:
        return f"{number} es un número impar."

number = int(input("Ingresa un número: "))
resultado = verify(number)
print(resultado)