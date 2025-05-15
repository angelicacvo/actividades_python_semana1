def find_max(values):
  if not values:
    return None
  return max(values)

my_values = [5, 2, 8, 1, 9, 3]
max_value = find_max(my_values)
if max_value is not None:
  print("El valor máximo en la lista es:", max_value)
else:
  print("La lista está vacía.")