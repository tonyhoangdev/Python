#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: Magic method for comparations
"""
'''
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=
'''
class SpecialString:
    def __init__(self, cont):
        self.cont = cont
    
    def __gt__(self, other):
        for i in range(len(other.cont) + 1):
            result = other.cont[:i] + ">" + self.cont
            result += ">" + other.cont[i:]
            print(result)

spam = SpecialString("spam")
hello = SpecialString("Hello world!")

spam > hello
