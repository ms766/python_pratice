#!/usr/bin/env python3

class Product:
    def __init__(self, price):
        self.price = price

    # getter
    @property
    def price(self):
        return self.__price

    # setter / if this is commented out then we have a read only class
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        self.__price = value


product = Product(10)
print(product.price)
