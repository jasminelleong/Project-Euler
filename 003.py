# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
from utilities import is_prime
import math


def largestPrimeFactor(n) :
    #factors = []
    for i in reversed(range(1, int(math.sqrt(n)))) :
        if i % 2 != 0 :
            if n % i == 0 :
                if is_prime(i) :
                    return i
    
    return 1

print (largestPrimeFactor(600851475143))