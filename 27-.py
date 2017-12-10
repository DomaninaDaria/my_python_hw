import random
s = "In any business the most important thing is to start no one has been able to succeed planning"
count = 0


def pemrtuate(text):
    lst = text.split(" ")
    print(lst)
    for i in range(len(lst)):
        lst2 = [] * 100
        index = (len(lst[i])-1)
        for j in range(1, len(lst[i])-1):
            lst2 += lst[i][j]
        random.shuffle(lst2)
        lst2.insert(0, lst[i][0])
        lst2.append(lst[i][index])
        print(lst2)
        lst[i] = "".join(lst2)
    print(" ".join(lst))


pemrtuate(s)





