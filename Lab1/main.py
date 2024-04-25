""" ---Greatest common divisor---
Implement 3 different algorithms for computing the GCD of 2 natural numbers.
One of the algorithm should work for numbers of arbitrary size!
Perform a comparative running time analysis of these algorithms for a set of at least 10 inputs(use appropriate time units in order to differentiate the algorithms)
"""
import math

def gcd_euclidean(a, b): #Euclidean Algorithm for small numbers
    #computes the GCD of 'a' and 'b' by repeatedly replacing the larger number with the remainder of its division by the smaller number,
    #and it continues until 'b' becomes zero. At that point, 'a' contains the GCD of the original 'a' and 'b' values.


    while b != 0:
        a, b = b, a % b
    return a

def gcd_binary(a, b): #Stein's Algorithm - optimization of the Eucliudean Algorithm to work with larger numbers
    if a == b: # base case when a = b, already the gcd
        return a
    if a == 0: # base case when a = 0, b is the gcd
        return b
    if b == 0: # base case when b = 0, a is the gcd
        return a

    # we do the following conditional checks until we get a base case
    if a % 2 == 0:  # If 'a' is even
        if b % 2 == 1:   # If 'b' is odd
            return gcd_binary(a // 2, b)
        else:
            return gcd_binary(a // 2, b // 2 ) // 2 # a and b are even
    if b % 2 == 0:  # If 'b' is even
        return gcd_binary(a, b // 2) # a is odd, b is even
    if a > b: # a and b are odd
        return gcd_binary((a - b) // 2, b)
    return gcd_binary(a, (b - a) // 2)

def extended_gcd(a, b): #for numbers of arbitrary size / extended Euclidean algorithm
    # the algorithm finds the GCD between a and b and the coefficients x and y s.t. gcd(a, b) = x * a + y * b
    if a == 0:
        return (b, 0, 1) # the special case where b = gcd(a,b) = 0 + b
    else:
        gcd, x, y = extended_gcd(b % a, a) #recursively calls extended_gcd with the arguments (b % a, a) until a becomes 0
        # to find the GCD and coefficients for the remainder of the division.
        return (gcd, y - (b // a) * x, x)

import random
import timeit

# Generate 10 random input pairs
input_data = [(random.randint(1, 1000), random.randint(1, 1000)) for _ in range(10)]

# Measure time for each algorithm
for a, b in input_data:
    print(f"Input: ({a}, {b})")
    print("The gcd is: ",gcd_euclidean(a,b))
    print("Euclidean Algorithm:", timeit.timeit(lambda: gcd_euclidean(a, b), number=10000 ),"seconds")
    print("Binary GCD Algorithm:", timeit.timeit(lambda: gcd_binary(a, b), number=10000), "seconds")
    print("Extended Euclidean Algorithm:", timeit.timeit(lambda: extended_gcd(a, b), number=10000), "seconds")
    print()

