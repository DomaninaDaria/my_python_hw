import random

list_of_used_values = []
list_of_values = [2, 3, 4, 5, 6, 7, 8, 9]
result = []
k = 0
while len(result) != 15:
    new_values_are_not_in_used_values_list = True
    index = 2 + k
    k += 1
    number_1 = random.choice(list_of_values)
    number2 = random.choice(list_of_values)
    list_of_used_values += [number_1, number2]
    for j in range(len(list_of_used_values) - index):
        if number_1 == list_of_used_values[2*j] and number2 == list_of_used_values[2*j + 1] \
                or number_1 == list_of_used_values[2*j + 1] and number2 == list_of_used_values[2*j]:
            new_values_are_not_in_used_values_list = False
            break

    if new_values_are_not_in_used_values_list:
        result.append(number_1 * number2)
        print("%d * %d = %d " % (number_1, number2, number_1 * number2))


