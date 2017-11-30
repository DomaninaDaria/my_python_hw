import random

print("Exercise 25")

c = 1
lst1 = [0] * 50
for i in range(50):
    lst1[i] = c
    c += 2

print(lst1)


def shuffle_list(list_to_shuffle):
    count = 0
    while count != 50:
        i = random.randrange(len(list_to_shuffle))
        temp = list_to_shuffle[i]
        list_to_shuffle[i] = list_to_shuffle[-1]
        list_to_shuffle[-1] = temp
        count += 1
    print(list_to_shuffle)


shuffle_list(lst1)


print("Exercise 26")


lst2 = [0] * 11
for i in range(11):
    lst2[i] = random.randint(-1, 1)
print(lst2)


def calc_frequency(lst):
    gr1 = 0
    gr2 = 0
    gr3 = 0
    for i in range(len(lst)):
        if lst[i] == -1:
            gr1 += 1
        elif lst[i] == 0:
            gr2 += 1
        elif lst[i] == 1:
            gr3 += 1
    if gr1 != gr2 and gr2 != gr3 and gr1 != gr3:
        max_group = max(gr1, gr2, gr3)
        if max_group == gr1:
            most_frequent = -1
        elif max_group == gr2:
            most_frequent = 0
        else:
            most_frequent = 1
    else:
        most_frequent = None

    return most_frequent


print("The most repeated number is %s" % calc_frequency(lst2))























