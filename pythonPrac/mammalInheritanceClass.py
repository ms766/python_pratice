#!/usr/bin/env python3

# Animal: parent, base
class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

# childern class


class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass


# m = Mammal()
# m.eat()
# m.walk()
# print(m.age)
# print(m.weight)
# print(isinstance(m, Mammal))
# print(isinstance(m, object))
# print(issubclass(Mammal, Animal))
# print(issubclass(Mammal, object))
