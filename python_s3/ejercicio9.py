def find_pairs(num_list):

  pair_list = []
  for num in num_list:
    if num % 2 == 0:
      pair_list.append(num)
  return pair_list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = find_pairs(numbers)
print(pairs)