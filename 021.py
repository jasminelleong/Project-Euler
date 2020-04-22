# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
# numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
# proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

from utilities import calculate_divisors


def get_proper_divisors(number):
    divisors = calculate_divisors(number)
    divisors.remove(number)
    return divisors


cumulative_amicable_sum = 0
numbers_to_test = list(range(3, 10000))

amicables = []

for i in numbers_to_test:
    divisors = get_proper_divisors(i)
    amicable_candidate = sum(divisors)
    if amicable_candidate == i:
        continue
    if sum(get_proper_divisors(amicable_candidate)) == i:
        cumulative_amicable_sum += i
        amicables.append(i)

print(cumulative_amicable_sum)
