#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: Class Data Hiding
"""

class Queue:
    """
    Weakly private methods and attributes have a
    single underscore at the begining
    "from module_name import *", won't import variables that start with a single underscore
    _hiddenlist: attr is marked as private, but it can still be accessed in the outside code
    __repr__: magic method is used for string representation of the instance 
    """
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

print("Weakly private")
queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
 

class Spam:
    """
    Strongly private methods and attributes have a double underscore
    __privatemethod of class Spam.
    _Spam__privatemethod: to accessed externally
    """
    __egg = 6
    def print_egg(self):
        print(self.__egg)
    
s = Spam()
s.print_egg()
print(s._Spam__egg)
# Accessing private method form external will cause AttributeError
# print(s.__egg)
