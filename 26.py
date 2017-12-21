import random
print("Exercise 26")


lst2 = [0] * 11
for i in range(11):
    lst2[i] = random.randint(-1, 1)
print(lst2)


def calc_frequency(lst):
    minus_one = 0
    zero = 0
    one = 0
    for i in range(len(lst)):
        minus_one = [lst.count(-1), -1]
        zero = [lst.count(0), 0]
        one = [lst.count(1), 1]
    are_not_same = minus_one[0] != zero[0] and zero[0] != one[0] and minus_one[0] != one[0]
    if are_not_same or zero[0] == 0 and minus_one[0] == 0 or zero[0] == 0 and one[0] == 0 or minus_one[0] == 0 or one[0] == 0:
        print(max(minus_one, zero, one)[1])
    else:
        print(None)

calc_frequency(lst2)