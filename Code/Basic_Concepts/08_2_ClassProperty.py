#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: Properties
"""
class Pizza:    
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    '''
    Create a property is pineapple_allowed (read-only)
    '''
    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    '''
    Property can also be set by defining setter/getter functions
    @func_name.setter
    '''
    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "allow":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)
