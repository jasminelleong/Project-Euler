# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
#
# [ Stuff that doesn't render correctly ]
#
# By expanding this for the first four iterations, we get:
#
# [ Stuff that doesn't render correctly ]
#
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example
# where the number of digits in the numerator exceeds the number of digits in the denominator.
#
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
from utilities import add_fractions, fraction_inverse

initial_fraction = add_fractions((1, 1), (1, 2))
seed_fraction = (1, 2)
expanded_fraction = seed_fraction
numerator_has_more_digits = 0

for i in range(1000):
    base = add_fractions((2, 1), (1, 2))
    for j in range(i):
        base = add_fractions((2, 1), fraction_inverse(base))

    base = add_fractions((1, 1), fraction_inverse(base))
    if len(str(base[0])) > len(str(base[1])):
        numerator_has_more_digits += 1
        # print('{}/{}'.format(base[0], base[1]))

print(numerator_has_more_digits)
