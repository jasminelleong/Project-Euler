# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves
# prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?
from utilities import is_prime, generate_rotations


def is_circular_prime(num):
    rotations = generate_rotations(i)
    # Don't check num for primeness again
    rotations.remove(num)
    for rotation in rotations:
        if not is_prime(rotation):
            return False
    return True


num_circular_primes = 0

for i in range(2, 1000000):
    if is_prime(i) and is_circular_prime(i):
        num_circular_primes += 1

print(num_circular_primes)
