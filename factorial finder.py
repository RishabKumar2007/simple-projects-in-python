import math
from math import factorial

def a(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n - 1))
number = int(input("Enter a number: "))
result = a(number)
print(f'The factorial of {number} is {result}')

