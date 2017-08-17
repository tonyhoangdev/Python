#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: Magic method for making classes act like containers
"""
'''
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g. in for loops)
__contains__ for in

__call__
__init__
__str__
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
