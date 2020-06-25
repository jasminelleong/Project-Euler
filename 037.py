# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
# left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
# 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from utilities import all_primes_up_to

primes_under_1m = set(all_primes_up_to(1000000))


def generate_left_or_right_truncatable_primes(truncatable_seed: int, prime_list: set, left: bool):
    truncatable_set = set()
    start_number = 0
    if left:
        start_number = 1
    for i in range(start_number, 10):
        if left:
            candidate = int(str(i) + str(truncatable_seed))
        else:
            candidate = (truncatable_seed * 10) + i

        if candidate in prime_list:
            truncatable_set.add(candidate)

    meta_set = truncatable_set.copy()
    for truncatable in truncatable_set:
        meta_set |= generate_left_or_right_truncatable_primes(truncatable, prime_list, left)

    return meta_set


truncatable_prime_seeds = [2, 3, 5, 7]

left_truncatable_primes = set()
right_truncatable_primes = set()

for seed in truncatable_prime_seeds:
    left_truncatable_primes |= generate_left_or_right_truncatable_primes(seed, primes_under_1m, True)
    right_truncatable_primes |= generate_left_or_right_truncatable_primes(seed, primes_under_1m, False)

truncatable_primes = [prime for prime in right_truncatable_primes if prime in left_truncatable_primes]

print(sum(truncatable_primes))
