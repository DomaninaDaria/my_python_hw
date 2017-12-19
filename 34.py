class Circle:
    def __init__(self, coord_x_circle, coord_y_circle, radius):
        self.coord_x_circle = coord_x_circle
        self.coord_y_circle = coord_y_circle
        self.radius = radius


class DotCoordinate:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y


def circle_function(x, y):
    our_circle_1 = Circle(4, 5, 7)
    if (x - our_circle_1.coord_x_circle)**2 + (y - our_circle_1.coord_y_circle)**2 <= our_circle_1.radius:
        print("dot is  in circle")
    else:
        print("dot is not in circle")


if __name__ == "__main__":
    our_dot_1 = DotCoordinate(int(input("Input x of dot 1: ")), int(input("Input y of dot 1: ")))
    circle_function(our_dot_1.coord_x, our_dot_1.coord_y)
    our_dot_2 = DotCoordinate(int(input("Input x of dot 2: ")), int(input("Input y of dot 2: ")))
    circle_function(our_dot_2.coord_x, our_dot_2.coord_y)

