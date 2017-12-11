import string
import random
s = "In any business the most important thing is to start, no one has been able to succeed planning!"
count = 0


def pemrtuate(text):
    lst = text.split(" ")
    print(lst)
    punctuation = string.punctuation
    print(punctuation)
    f = True
    for i in range(len(lst)):
        lst2 = [] * len(lst[i])
        index = (len(lst[i])-1)
        for j in range(len(punctuation)):
            if lst[i][index] == punctuation[j]:
                f = False
        if(f):
            lst2 += lst[i][1:-1]
        else:
            lst2 += lst[i][1:-2]
        random.shuffle(lst2)
        lst2.insert(0, lst[i][0])
        if(f):
            lst2.append(lst[i][index])
        else:
            lst2.append(lst[i][index - 1])
            lst2.append(lst[i][index])
        lst[i] = "".join(lst2)
    print(" ".join(lst))


pemrtuate(s)





