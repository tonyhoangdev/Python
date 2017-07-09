#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: Class
"""

class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

class Dog:
    legs = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")

## Cat objects
print("=== Class Cat ===")
felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown" , 3)

print("Color: {0}, Legs: {1}".format(felix.color, felix.legs))
print("Color: {0}, Legs: {1}".format(rover.color, rover.legs))
print("Color: {0}, Legs: {1}".format(stumpy.color, stumpy.legs))

## Dog objects
print("=== Class DOG ===")
fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

# Attribute
print(fido.legs)
print(Dog.legs)
