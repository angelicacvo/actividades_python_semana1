def sum_unique(numbers_list):
    unique_set = set(numbers_list)
    total = sum(unique_set)
    return total

numbers = [1, 2, 3, 2, 4, 1, 5]
unique_sum = sum_unique(numbers)
print(f"La suma de los elementos únicos es: {unique_sum}")
