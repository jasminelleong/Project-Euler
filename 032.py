# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for
# example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is
# 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9
# pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from utilities import all_string_permutations

all_one_through_nine_pandigitals = all_string_permutations('987654321')

unique_products = set()

for pandigital in all_one_through_nine_pandigitals:
    for i in range(1, 8):
        for j in range(i + 1, 9):
            if int(pandigital[:i]) * int(pandigital[i:j]) == int(pandigital[j:]):
                print('{} * {} == {}'.format(pandigital[:i], pandigital[i:j], pandigital[j:]))
                unique_products.add(int(pandigital[j:]))

print(sum(unique_products))
