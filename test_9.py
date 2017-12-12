value = int(input("Input value of elements in list: "))
lst = [0] * value
for i in range(value):
    print("Input element in list number", i+1)
    lst[i] = int(input())
print(lst)
max_value = 0
for i in range(value):
    if abs(lst[i]) > max_value:
        max_value = abs(lst[i])
for i in range(value):
    lst[i] /= max_value
    lst[i] = round(lst[i], 2)
print(lst)

