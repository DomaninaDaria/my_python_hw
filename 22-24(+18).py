import random
print("--------------------------------22--------------------------------")


def group_by_surname(list_of_enrollees):
    group1 = group2 = group3 = group4 = 0
    for student in list_of_enrollees:
        first_surname_letter = student.split(" ")[1]
        if "A" <= first_surname_letter <= "I":
            group1 += 1
        elif "J" <= first_surname_letter <= "P":
            group2 += 1
        elif "Q" <= first_surname_letter <= "T":
            group3 += 1
        else:
            group4 += 1
    return group1, group2, group3, group4


names = ['Ann Z', 'Bob J', 'Ken A', 'Lili T', "Tom Z"]
print("numbers of student in 1 group=%d; 2 group = %d; 3 group = %d; 4 group = %d." % group_by_surname(names))


print("--------------------------------23--------------------------------")
number_of_computer = random.randint(1, 10)
number_of_user = int(input('Input number from 1 to 10:'))
if number_of_user < 1 or number_of_user > 10:
    print("You have chosen wrong number")
else:
    while number_of_user != number_of_computer:
        if number_of_user < number_of_computer:
            number_of_user = int(input("Input bigger number:"))
        else:
            number_of_user = int(input("Input smaller number:"))

    print("You are right, my number is ", number_of_user)


print("--------------------------------24--------------------------------")


def chess_reward():
    corn = 1
    cell = 0
    while corn <= 1000000:
        corn *= 2
        cell += 1
    return cell, corn - 1


print("На %d клетке количество зерен будет больше 1 000 000, а именно = %d" % chess_reward())


print("--------------------------------18--------------------------------")

def sum_symbol_codes(first, last):
    first_symbol = ord(first)
    last_symbol = ord(last)
    counter = 0
    for quantity in range(first_symbol, last_symbol+1):
        counter += quantity
    return counter

print(sum_symbol_codes("A", "B"))

