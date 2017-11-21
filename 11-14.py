import math


print("Exercise number 11")


def degrees_in_radians(degrees):
    return (degrees * math.pi) / 180


degrees1 = 45
degrees2 = 40
degrees3 = 60
print("Cos of degrees(%d)= %.4f" % (degrees1, math.cos(degrees_in_radians(degrees1))))
print("Cos of degrees(%d)= %.4f" % (degrees2, math.cos(degrees_in_radians(degrees2))))
print("Cos of degrees(%d)= %.4f" % (degrees3, math.cos(degrees_in_radians(degrees3))))
print("------------------------------------------------------------------------")


print("Exercise number 12")


def sum_of_figures(number):
    return number % 10 + number % 100 // 10 + number // 100


number1 = int(input("Input three-digit number: "))
if number1 // 1000 == 0:
    print("Sum of figures is: ", sum_of_figures(number1))
else:
    print("You entered more than three-digit number!")


def square_perimeter(cathetus_1, cathetus_2):
    return cathetus_1 * cathetus_2 * 1/2, cathetus_1 + cathetus_2 + math.sqrt(cathetus_1**2 + cathetus_2**2)


print("------------------------------------------------------------------------")
print("Exercise number 13")
side_1 = int(input("Input value of cathetus 1 : "))
side_2 = int(input("Input value of  cathetus 2: "))
if side_1 <= 0 or side_2 <= 0:
    print("Error, sides of rectangle can not be <0 or =0")
else:
    print("Square of rectangle is %.2f and Perimeter of rectangle is %.2f" % (square_perimeter(side_1, side_2)))
   

def even_or_not(number):
    return number % 2 == 0


print("------------------------------------------------------------------------")
print("Exercise number 14")
n = int(input("Input the number"))
if even_or_not(n):
    print("Number %d is even" % n)
else:
    print("Number %d is not even" % n)




