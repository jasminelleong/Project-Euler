# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For
# example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

from utilities import is_prime, all_string_permutations, is_permutation


def is_pandigital(num: int) -> bool:
    num_string = str(num)
    if len(num_string) > 9:
        return False

    permuted_pandigital = ''.join([str(i + 1) for i in range(len(num_string))])
    return is_permutation(num_string, permuted_pandigital)


pandigital_string = '987654321'

pandigitals = []

for i in range(9):
    pandigitals.extend([int(perm) for perm in all_string_permutations(pandigital_string[i:len(pandigital_string)])])

pandigitals = reversed(sorted(pandigitals))

for pandigital in pandigitals:
    if is_prime(pandigital):
        print(pandigital)
        exit(0)