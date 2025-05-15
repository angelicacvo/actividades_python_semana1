# Diseñar un sistema que permita registrar compras de boletos de pasajeros, su destino, equipaje, y calcular el costo total del viaje, asignando un ID único por reserva para hacer seguimiento. El sistema debe validar los límites de peso, aplicar cobros por equipaje y generar un resumen detallado.

from datetime import datetime

base_prices = {
    "nacional": {"destino": "Bogotá → Medellín", "precio": 230000},
    "internacional": {"destino": "Bogotá → España", "precio": 4200000}
}

def calculate_main_luggage_cost(weight):
    if weight <= 20:
        return 50000, "Admitido"
    elif weight <= 30:
        return 70000, "Admitido"
    elif weight <= 50:
        return 110000, "Admitido"
    else:
        return 0, "No admitido (Debe cancelar o viajar sin equipaje principal)"

def validate_hand_luggage(weight):
    if weight <= 13:
        return "Admitido"
    else:
        return "Rechazado"

def generate_id(number):
    return f"COMP{number:04d}"

purchases = []
purchase_counter = 0

def register_purchase():
    global purchase_counter

    name = input("Ingrese el nombre del pasajero: ")
    trip_type = input("Tipo de viaje (nacional/internacional): ").lower()

    if trip_type not in base_prices:
        print("❌ Tipo de viaje inválido. Intente de nuevo.")
        return

    try:
        main_weight = float(input("Peso del equipaje principal (kg): "))
        has_hand = input("¿Lleva equipaje de mano? (si/no): ").lower()

        hand_weight = 0
        if has_hand == "si":
            hand_weight = float(input("Peso del equipaje de mano (kg): "))

        trip_date = input("Ingrese la fecha del viaje (YYYY-MM-DD): ")

        luggage_cost, main_status = calculate_main_luggage_cost(main_weight)
        hand_status = validate_hand_luggage(hand_weight)

        if main_status.startswith("No admitido"):
            print("⚠️ Advertencia: Su equipaje principal no es admitido. Se registrará la compra sin costo de equipaje principal.")
            luggage_cost = 0

        purchase_counter += 1
        purchase_id = generate_id(purchase_counter)

        base_price = base_prices[trip_type]["precio"]
        total = base_price + luggage_cost

        purchase = {
            "id": purchase_id,
            "nombre": name,
            "destino": base_prices[trip_type]["destino"],
            "tipo_viaje": trip_type,
            "fecha": trip_date,
            "estado_principal": main_status,
            "estado_mano": hand_status,
            "total": total
        }

        purchases.append(purchase)

        print("\n=====================")
        print("✅ COMPRA REGISTRADA")
        print("=====================")
        print(f"ID de compra (Guárdelo bien): ** {purchase_id} **")
        print(f"Nombre del pasajero: {name}")
        print(f"Destino: {base_prices[trip_type]['destino']}")
        print(f"Fecha: {trip_date}")
        print(f"Estado del equipaje principal: {main_status}")
        print(f"Estado del equipaje de mano: {hand_status}")
        print(f"Costo total del viaje: ${total:,.0f}")
        print("=====================\n")

    except ValueError:
        print("❌ Error: Ingreso inválido. Intente de nuevo.")

def check_purchase():
    search_id = input("Ingrese el ID de compra a consultar (ejemplo COMP0001): ").upper()
    for p in purchases:
        if p["id"] == search_id:
            print("\n--- Detalle de la compra ---")
            print(f"ID de compra: {p['id']}")
            print(f"Nombre del pasajero: {p['nombre']}")
            print(f"Destino: {p['destino']}")
            print(f"Fecha: {p['fecha']}")
            print(f"Estado del equipaje principal: {p['estado_principal']}")
            print(f"Estado del equipaje de mano: {p['estado_mano']}")
            print(f"Costo total del viaje: ${p['total']:,.0f}")
            return
    print("❌ ID no encontrado. Revise que esté bien escrito.")

def list_purchases():
    if not purchases:
        print("⚠️ No hay compras registradas aún.")
        return
    print("\n=== LISTADO DE COMPRAS ===")
    for p in purchases:
        print(f"ID: {p['id']} | Nombre: {p['nombre']} | Destino: {p['destino']} | Fecha: {p['fecha']} | Total: ${p['total']:,.0f}")
    print("===========================\n")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar compra")
        print("2. Consultar compra por ID")
        print("3. Ver todas las compras registradas")
        print("4. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            register_purchase()
        elif option == "2":
            check_purchase()
        elif option == "3":
            list_purchases()
        elif option == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

menu()



