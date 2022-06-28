"""
Factorials 
4! is 4x3x2x1
4 x 3!"""

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

factorial(4)

"""to debug, add debug dot on factorial(4) and open up the run and debug console"""