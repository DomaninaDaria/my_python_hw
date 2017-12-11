print("--------------------------8-----------------------------")
n = int(input("Input value of elements in list "))
our_lst = [0] * n
for i in range(n):
    print("Input value of element number ", i+1)
    our_lst[i] = int(input())
print(our_lst)
maximum = our_lst[0]
minimum = our_lst[0]
index_max = 0
index_min = 0
for i in range(n):
    if our_lst[i] > maximum:
        maximum = our_lst[i]
        index_max = i

    if our_lst[i] < minimum:
        minimum = our_lst[i]
        index_min = i

our_lst[index_max] = minimum
our_lst[index_min] = maximum
print(our_lst)



