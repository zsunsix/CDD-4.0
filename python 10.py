def remove_repetidos(list_):
    return sorted(set(list_))

number_list = [1,2,2,3,4,4,5,3,6,7,6,8]
new_list = remove_repetidos(number_list)

print(new_list)

