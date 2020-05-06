# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced
# proper fraction.
#
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
#
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that 2/5 is the fraction immediately to the left of 3/7.
#
# By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of
# the fraction immediately to the left of 3/7.

import math

from utilities import reduce_fraction_to_simplest_terms

candidate_fractions = []

for d in range(1, 1000001):
    below_three_sevenths_d = math.floor(3 / 7 * d) - 1
    if below_three_sevenths_d <= 0:
        below_three_sevenths_d = 1
    three_sevenths_d = math.ceil(3 / 7 * d)
    for n in range(below_three_sevenths_d, three_sevenths_d):
        if n / d < 3 / 7:
            candidate_fractions.append((n, d))

candidate_fractions = sorted(candidate_fractions, key=lambda x: x[0] / x[1])
print(reduce_fraction_to_simplest_terms(candidate_fractions[-1]))
