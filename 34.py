import math


class Circle:
    def __init__(self, coord_x_circle, coord_y_circle, radius_circle):
        self.coord_x_circle = coord_x_circle
        self.coord_y_circle = coord_y_circle
        self.radius = radius_circle

    def is_dot_in_circle(self, point):

        if math.sqrt((point.coord_x - self.coord_x_circle) ** 2 + (point.coord_y - self.coord_y_circle) ** 2) <= self.radius:
            print("point is in circle")
        else:
            print("point is not in circle")

class DotCoordinate:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y


if __name__ == "__main__":
    our_circle_1 = Circle(4, 5, 7)
    our_dot_1 = DotCoordinate(int(input("Input x of point 1: ")), int(input("Input y of point 1: ")))
    our_circle_1.is_dot_in_circle(our_dot_1)

