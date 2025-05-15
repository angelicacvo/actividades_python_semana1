def fizzbuzz(number):
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

while True:
    try:
        number = int(input("Ingresa un número: "))
        if number > 0:
            break
        else:
            print("El número debe ser mayor que cero.")
    except ValueError:
        print("Ingresa un número entero válido.")

fizzbuzz(number)
