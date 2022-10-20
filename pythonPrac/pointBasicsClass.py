#!/usr/bin/env python3

class Point:
    default_color = "red"

    # instance methods
    def __init__(self, x, y):
        # self is a ref to the current point obj
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point ({self.x}, {self.y})"

    def draw(self) -> str:
        print(f"point ({self.x}, {self.y})")

    # factory method

    @classmethod
    def zero(cls):
        cls(0, 0)


#########################################################
Point.default_color = "yellow"
p = Point(4000, 2)
o = Point(3, 4440)
p.draw()
print(p.x)
print(p.default_color)
p.z = 10
print(p.z)
p.zero()
print(str(p))
print(p == o)

point = Point(2, 20)
other = Point(1, 2)
print(point == other)
print(point > other)
print(point + other)
combined = point + other
print(combined)
