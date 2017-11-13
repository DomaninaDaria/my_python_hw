import math
a = 7
b = 9
c = 13
d = a + b*(c/2)
print("------------------------")
print("1.")
print("%d + %d * (%d/2) = %.3f" % (a, b, c, d))
print("------------------------")


print("2.")
d = (pow(a, 2) + b**2) % 2
print(" (%d^2 + %d^2)%%2 = %d " % (a, b, d))
print("------------------------")


print("3.")
d=(a + b)/12 * c % 4 + b
print("(%d + %d)12 * %d%%4 + %d = %.3f " % (a, b, c, b, d))
print("------------------------")


print("4.")
d = (a-b * c)/(a + b) % c
print("(%d-%d * %d)/(%d + %d)%%%d = %.3f" % (a, b, c, a, b, c, d))
print("------------------------")


print("5.")
c = math.radians(180)
d = abs(a-b)/pow((a + b), 3) - math.cos(c)
print("|%d-%d|/(%d + %d)^3-cos(%f) = %.5f" % (a, b, a, b, c, d))
print("------------------------")


print("6.1")
c = 13
a = -15
print("(ln(1 + %d)/(-%d))^4 + |%d| = " % (c, b, a))
if(1+c) >= 0:
    d = (pow(math.log1p(1 + c) / (-b), 4) + abs(a))
    print("result is %.3f" % d)
else:
    print("error, the base of log. is <=0")
print("------------------------")


print("6.2")
c = -13
print("(ln(1 + %d)/(-%d))^4 + |%d| = " % (c, b, a))
if(1+c) >= 0:
    d = (pow(math.log1p(1 + c) / (-b), 4) + abs(a))
    print("(ln(1 + %d)/(-%d))^4 + |%d| = %.3f" % (c, b, a, d))
else:
    print("error, (1+%d)<=0" % c)
print("------------------------")


