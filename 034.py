# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math

cumulative_curious_numbers = 0

# Don't know how to prove the upper limit here, but trial and error led to the solution
for i in range(10, 100000):
    string_num = str(i)
    digit_factorial_sum = 0
    for digit in string_num:
        digit_factorial_sum += math.factorial(int(digit))
        if digit_factorial_sum > i:
            break

    if digit_factorial_sum == i:
        print(i)
        cumulative_curious_numbers += i

print(cumulative_curious_numbers)
