import math
from math import log

def x(a):
    square_root = math.sqrt(a)
    return square_root
def y(a):
    natural_logarithm = math.log(a)
    return natural_logarithm
def z(a):
    sine_value = math.sin(a)
    return sine_value

a = float(input("Enter a number: "))

print(f'The square root of {a} is {x(a)}')
print(f'log of {a} is {y(a)}')
print(f'sine of {a} is {z(a)}')
