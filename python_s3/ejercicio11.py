def factorial(number):
    if number < 0:
        return None  
    elif number == 0:
        return 1  
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

while True:
    try:
        number = int(input("Ingresa un número entero positivo: "))
        break 
    except ValueError:
        print("La entrada debe ser un número entero.")

factorial_result = factorial(number)

if factorial_result is not None:
    print(f"El factorial de {number} es {factorial_result}")
else:
    print("No se puede calcular el factorial de números negativos.")
