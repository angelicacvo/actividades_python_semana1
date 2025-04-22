primer_numero = int(input("Ingresa el primer número "))
segundo_numero = int(input("Ingresa el segundo número "))

def comparar_numeros():
    if primer_numero > segundo_numero:
        print (primer_numero, " es mayor a ", segundo_numero)
    elif primer_numero < segundo_numero:
        print(primer_numero, " es menor a ", segundo_numero)
    else:
        print(primer_numero, " es igual a ", segundo_numero)

comparar_numeros()