

lst1 = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(lst1)
string = input("Input your string:")
string_ = string.lower()
print(string_)


def encode(str_to_encode):
    str1 = ""
    for i in range(len(str_to_encode)):
        for j in range(len(lst1)):
            if str_to_encode[i] == str(lst1[j]):
                if (j+5) < (len(lst1) - 1):
                    str1 += str(lst1[j+5])
                else:
                    p = len(lst1)-j
                    str1 += str(lst1[5 - p])
    return str1


print("Encoded string is:", encode(string_))