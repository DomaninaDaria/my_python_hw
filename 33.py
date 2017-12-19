import random


class Godzilla:
    def __init__(self, size_of_stomach):
        self.capacity = size_of_stomach


min_weight = 50
max_weight = 100


def main():
    def eat(weight_of_human):
        godzilla_1 = Godzilla(700)
        empty_place_that_has_to_remain = godzilla_1.capacity / 10
        while godzilla_1.capacity > empty_place_that_has_to_remain:
            if (godzilla_1.capacity - weight_of_human) > empty_place_that_has_to_remain:
                print("%d - %d " % (godzilla_1.capacity, weight_of_human))
                godzilla_1.capacity -= weight_of_human
                print("empty place = ", godzilla_1.capacity)
            elif (godzilla_1.capacity - min_weight) > empty_place_that_has_to_remain:
                print("We have to find a human with certain weight = ", godzilla_1.capacity - empty_place_that_has_to_remain)
                godzilla_1.capacity -= godzilla_1.capacity - empty_place_that_has_to_remain
                print("We eat him/ her, so, godzilla_1 is full")
                break
            else:
                print("Godzilla is full")
                break
    eat(random.randint(min_weight, max_weight))


if __name__ == "__main__":
    main()



