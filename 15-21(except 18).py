import math
import random


print("Exercise 15")


def circles_intersection(x1, y1, r1, x2, y2, r2):
    s = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return s < (r1 + r2) and s > math.fabs(r2 - r1) or (s == 0 and r1 == r2) or (s == r1 + r2)


x_2 = int(input("Input value of x2: "))
x_1 = int(input("Input value of x1: "))
y_2 = int(input("Input value of y2: "))
y_1 = int(input("Input value of y1: "))
r1 = 0
r2 = 0
while r1 <= 0:
    r1 = int(input("Input value of r1: "))
while r2 <= 0:
    r2 = int(input("Input value of r2: "))


if circles_intersection(x_1, y_1, r1, x_2, y_2, r2):
    print("Circles intersect!")
else:
    print("Circles do not intersect!")


print("Exercise 16")





def have_trains_crashed(v1, v2):
    return 4 / v1 >= 6 / v2


speed1 = 0
speed2 = 0
while speed1 <= 0 or speed2 <= 0:
    speed1 = int(input("Input speed of first train:"))
    speed2 = int(input("Input speed of second train: "))


if have_trains_crashed(speed1, speed2):
    print('trains won`t have crashed!')
else:
    print('trains will have crashed')

print("Exercise 17")


def solve_quadratic_equation(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = round(((-b) + math.sqrt(d)) / (2 * a), 3)
        x2 = round(((-b) - math.sqrt(d)) / (2 * a), 3)
    elif d == 0:
        x1 = round((-b) / (2*a), 3)
        x2 = None
    else: x1 = x2 = None
    return x1, x2


print("First root of the equation = %s, second = %s." % solve_quadratic_equation(4, 5, -7))




print("Exercise 19")


def find_min_max_diff(num_limit, lower_bound, upper_bound):
    curr_max = lower_bound
    curr_min = upper_bound
    for i in range(num_limit):

        rand_number = random.randint(lower_bound, upper_bound)
        print("We have number %d = " % (i+1), rand_number)

        if curr_max < rand_number:
            curr_max = rand_number

        if curr_min > rand_number:
            curr_min = rand_number
    print("MAX = ", curr_max)
    print("MIN = ", curr_min)

    return curr_max - curr_min


quantity_of_numbers = int(input("Input quantity if numbers: "))
low = int(input("Input lower bound: "))
up = int(input("Input upper bound: "))
print("max number - min number =", find_min_max_diff(quantity_of_numbers, low, up))

print("Exercise 20")


def diff_even_odd(lower_bound, upper_bound):
    num_limit = 100
    count_even = 0
    count_not_even = 0
    for i in range(num_limit):
        rand_number = random.randint(lower_bound, upper_bound)
        print('Number %d = ' % (i+1), rand_number)

        if rand_number % 2 == 0:
            count_even += rand_number
        else:
            count_not_even += rand_number

    print("Amount of even figures = ", count_even)
    print("Amount of not even figures = ", count_not_even)
    return count_even - count_not_even


print("Amount of even figures - amount of not even figures = ", diff_even_odd(4, 99))


print("Exercise 21")


def get_max_digit(number):
    max_digit = 0
    for i in range(len(str(number))):
        figure = number % 10
        number = number // 10
        if max_digit < figure:
            max_digit = figure

    return max_digit


number1 = int(input("Input your number: "))
print("MAX digit is:", get_max_digit(number1))
















