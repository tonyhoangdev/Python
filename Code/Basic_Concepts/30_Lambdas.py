#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: Lambdas
"""

def my_func(f, arg):
    return f(arg)

x = my_func(lambda x: 2*x*x, 6)
print(x)

# named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(4))

# lambda
print((lambda x: x**2 + 5*x + 4)(4))

# assigned to variables
double = lambda x: x * 2
print(double(4))
