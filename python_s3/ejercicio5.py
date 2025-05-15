def convert_temperature(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

try:
  celsius_grades = float(input("Ingrese la temperatura en grados Celsius: "))
except ValueError:
  print("Entrada inválida. Por favor, ingrese un número.")
  exit()
fahrenheit_grades = convert_temperature(celsius_grades)
print(f"La temperatura {celsius_grades}°C es igual a {fahrenheit_grades}°F")