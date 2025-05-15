def remove_duplicates(original_list):
    new_list = []
    for item in original_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

my_list = [1, 2, 3, 2, 4, 1, 5]
list_without_duplicates = remove_duplicates(my_list)
print(list_without_duplicates)
