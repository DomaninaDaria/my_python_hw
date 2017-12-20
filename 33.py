import random

MIN_WEIGHT = 50
MAX_WEIGHT = 100


class Godzilla:
    def __init__(self, size_of_stomach, name):
        self.capacity = size_of_stomach #700
        self.name = name
        self.empty_capacity = self.capacity/100*90  #630

    def print_info(self):
        print("Hello, i am Godzilla, my name is %s and i would like to eat some people, capacity of my stomach is %d " %(self.name, self.capacity))

    def eat(self):
        print("My capacity of stomach that i want to fill =", self.capacity)
        while self.empty_capacity != 0:
            # input(print("if you would like to feed me, you just have to press enter and we will find a food:"))
            person_weight = random.randint(MIN_WEIGHT, MAX_WEIGHT)
            if (self.empty_capacity - person_weight) > 0:
                print("We found a human with weight = %d, so, empty capacity in my stomach = %d " % (person_weight, self.empty_capacity - person_weight))
                print("I want more")
                print()
                self.empty_capacity -= person_weight

            elif (self.empty_capacity - MIN_WEIGHT) > 0:
                print("We have to find a human with certain weight = ", self.empty_capacity)
                self.empty_capacity -= self.empty_capacity
                print("I eat him/ her, so, empty place of my stomach = %d and i am full!" % self.empty_capacity)
                break
            else:
                print("Godzilla %s is full" % self.name)
                break


if __name__ == "__main__":
    godzilla_1 = Godzilla(700, "Blake")
    godzilla_1.print_info()
    godzilla_1.eat()



