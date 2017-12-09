

encode_list = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print(encode_list)
string = input("Input your string:")
string_ = string.lower()
print(string_)


def encode(str_to_encode):
    result = ""
    for i in range(len(str_to_encode)):
        for j in range(len(encode_list)):
            if str_to_encode[i] == encode_list[j]:
                result += str(encode_list[(j + 5) % len(encode_list)])
    return result


print("Encoded string is:", encode(string_))