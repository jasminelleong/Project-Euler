# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
from utilities import prime_factorization


def has_four_distinct_prime_factors(num):
    return len(set(prime_factorization(num))) == 4


for i in range(2, 1000000):
    if has_four_distinct_prime_factors(i) \
            and has_four_distinct_prime_factors(i + 1) \
            and has_four_distinct_prime_factors(i + 2) \
            and has_four_distinct_prime_factors(i + 3):
        print(i)
        exit(0)
