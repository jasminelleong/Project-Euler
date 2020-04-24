# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For
# example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

from utilities import is_prime, all_string_permutations

pandigital_string = '987654321'

pandigitals = []

for i in range(9):
    pandigitals.extend([int(perm) for perm in all_string_permutations(pandigital_string[i:len(pandigital_string)])])

pandigitals = reversed(sorted(pandigitals))

for pandigital in pandigitals:
    if is_prime(pandigital):
        print(pandigital)
        exit(0)