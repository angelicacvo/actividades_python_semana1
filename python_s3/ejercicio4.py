def verify_age():
    age = int(input("Ingresa tu edad "))
    if age >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
        
verify_age()