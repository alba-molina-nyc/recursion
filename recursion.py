"""
Factorials 
4! is 4x3x2x1
4 x 3!"""

def factorial(n):
    if n == 1:
        print(1)
        return 1
    return n * factorial(n-1)

factorial(4)