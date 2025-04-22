total_cuenta = int(input("¿Cuál es el total de la cuenta? "))
porcentaje_propina = int(input("¿Que porcentaje de propina quiere dejar? "))

def calcular_propina():
    total_propina = (total_cuenta * porcentaje_propina) / 100
    valor_total = total_cuenta + total_propina
    print("El valor total de su cuenta es: ", valor_total)

calcular_propina()


