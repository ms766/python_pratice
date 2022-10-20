#!/usr/bin/env python3

class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass


class Person:
    def greet(self):
        print("Person Greet")


class Employee:
    def greet(self):
        print("Employee Greet")


class Manager(Person, Employee):
    pass


m = Manager()

m.greet()
