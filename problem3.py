#!/usr/bin/python
''' Find's the highest prime factor using Fermat's Factorization'''

import math
import sys

def is_square(n):
    '''Returns true if n is a perfect squre.'''

    sqrt_n = math.floor(math.sqrt(n))
    return n == sqrt_n * sqrt_n

def find_prime_factor(n):
    '''Find largest prime factor.'''

    if n % 2 == 0:
        n = n +1
        sys.exit(-1)

    sqrt_n = math.sqrt(n)
    a = math.ceil(sqrt_n)
    b2 = a*a - n

    while not is_square(b2):
        #a += 1
        #b2 = a*a - n
        b2 = b2 + 2*a + 1
        a = a + 1

    return a + math.sqrt(b2)

if __name__ == "__main__":
    number = int(raw_input("Number >> "))
    print find_prime_factor(number)
