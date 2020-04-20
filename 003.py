# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

from utilities import is_prime

big_number = 600851475143
largest_possible_factor = int(math.sqrt(big_number))

# Iterate backwards from the square root of the big number
i = largest_possible_factor
while i > 1:
    if is_prime(i) and big_number % i == 0:
        # This is the largest prime factor
        print(i)
        exit(0)

    i -= 1
