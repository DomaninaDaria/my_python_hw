import random


class Godzilla:
    def __init__(self, size_of_stomach):
        self.V = size_of_stomach


def main():
    godzilla_1 = Godzilla(700)
    while godzilla_1.V > 70:
        weight_of_human = random.randint(50, 100)
        if (godzilla_1.V - weight_of_human) > 70:
            print("%d - %d " % (godzilla_1.V, weight_of_human))
            godzilla_1.V -= weight_of_human
            print("empty place = ", godzilla_1.V)
        elif (godzilla_1.V - 50) > 70:
            print("We have to find a human with certain weight = ", godzilla_1.V - 70)
            while weight_of_human != (godzilla_1.V - 70):
                weight_of_human = random.randint(50, 100)
            godzilla_1.V -= godzilla_1.V - 70
            print("We eat him/ her, so, godzilla_1 is full")
            break
        else:
            print("Godzilla is full")
            break


if __name__ == "__main__":
    main()



