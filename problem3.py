#!/usr/bin/python
import sys

def find_prime(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return n

if __name__ == "__main__":
    number = raw_input("Number>>")
    try:
        number = int(number)
    except ValueError,TypeError:
        print "Not a valid number{0}".format(number)
        sys.exit(-1)

    print find_prime(number)
