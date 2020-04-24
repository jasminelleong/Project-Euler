# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (
# i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

from utilities import is_prime, is_permutation

four_digit_primes = [i for i in range(1000, 10000) if is_prime(i)]
answer = None


for i in range(len(four_digit_primes)):
    for j in range(i + 1, len(four_digit_primes)):
        first_prime = four_digit_primes[i]
        second_prime = four_digit_primes[j]
        if not is_permutation(second_prime, first_prime):
            continue
        third_candidate = second_prime + (second_prime - first_prime)
        if is_prime(third_candidate) and is_permutation(third_candidate, second_prime):
            print(first_prime, second_prime, third_candidate)
