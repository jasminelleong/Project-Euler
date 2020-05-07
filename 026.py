# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2
# to 10 are given:
#
#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring
# cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

from bigfloat import *

largest_cycle_denominator = 0
largest_cycle_length = 0

setcontext(precision(10000))
for i in range(1, 1000):
    big_decimal = str(1 / BigFloat(i))
    right_substring_limit = 3
    while big_decimal[2:right_substring_limit] in big_decimal[right_substring_limit:]:
        right_substring_limit += 1
        substring = big_decimal[2:right_substring_limit]
        next_potential_cycle = big_decimal[right_substring_limit: right_substring_limit + len(substring)]
        if substring == next_potential_cycle:
            break

    cycle = big_decimal[2:right_substring_limit]
    print('1/{}: {}'.format(i, cycle))
    if len(cycle) > largest_cycle_length:
        largest_cycle_length = len(cycle)
        largest_cycle_denominator = i

print('Largest cycle was in 1/{}, {} digits.'.format(largest_cycle_denominator, largest_cycle_length))
