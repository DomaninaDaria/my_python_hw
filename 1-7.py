print('----------------------1.2.3------------------------')
a = round(float(input("Input value of a ")), 3)
b = round(float(input("Input value of b")), 3)
c = round(float(input("Input value of c")), 3)
result = round((a + b + c)**2, 3)
print("(%.3f + %.3f + %.3f)^2 = %.3f" % (a, b, c, result))


a = round(float(input("Input value of a ")), 3)
b = round(float(input("Input value of b")), 3)
g = float(input("Input value of g > 0 or g < 0 "))
while g == 0:
    g = float(input("Input value of g > 0 or g < 0 "))

result = round(a - 4*b / c, 3)
print("%.3f - 4*%.3f / %.3f = %.3f" % (a, b, c, result))


a = round(float(input("Input value of a ")), 3)
b = round(float(input("Input value of b")), 3)
c = round(float(input("Input value of c")), 3)
if (c - 1) == 0:
     print("Error")
else:
    result = round((a*b + 4) / (c - 1), 3)
    print("(%.3f*%.3f + 4) / (%.3f - 1) = %.3f" % (a, b, c, result))



print("-------------------------4------------------------")


number = int(input("Input number : "))

def amount_of_not_even_digits(value):
    sum = 0
    while value != 0:
        if (value % 10) % 2 != 0:
            sum += value % 10
        value //= 10
    return sum

print("sum of not even digits is ", amount_of_not_even_digits(number))

import math


print("-------------------------5------------------------")
our_number = 10
your_number_1 = float(input("Input number 1: "))
your_number_2 = float(input("Input number 2: "))
if abs(our_number - your_number_1) < abs(our_number - your_number_2):
    print("Number 1 is nearer than number 2, number 1 = ", your_number_1 )
elif abs(our_number - your_number_1)> abs(our_number - your_number_2):
    print("Number 2 is nearer than number 1, number 2 = ", your_number_2)
else:
    print("Same distance")

print("-------------------------6------------------------")
string1 = "downstream up"
string2 = "изограмма"


def isogram(string):
    f = False
    for i in range(0, len(string)-1):
         for j in range(i+1, len(string)):
            if string[i] == string[j] and string[i] != " ":
                f = True

    if f:
        print("Your string is not isogram")
    else:
        print("Your string is isogram")


isogram(string1)
isogram(string2)

print("-------------------------7------------------------")


def sum_of_fib(amount):
    fib_list = [0, 1]
    for i in range(2, amount):
        fib_list.append(fib_list[i-1] + fib_list[i - 2])
    our_sum = sum(fib_list)
    return our_sum

print(sum_of_fib(10))








