#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: Magic method for common operators
"""
'''
x + y = x.__add__(y)
if x and y different types, then y.__radd__(x)

__add__ for +
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **

__and__ for &
__xor__ for ^
__or__ for |
'''
class SpecialString:
    def __init__(self, cont):
        self.cont = cont
    
    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

    def __add__(self, other):
        return self.cont + ": " + other.cont

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)
print(spam + hello)
