# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this
# sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
# of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can
# be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is
# less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
from utilities import get_proper_divisors


def is_abundant(number):
    if sum(get_proper_divisors(number)) > number:
        return True
    return False


abundant_numbers = set()

for i in range(1, 28123):
    if is_abundant(i):
        abundant_numbers.add(i)

sorted_abundant_numbers = sorted(list(abundant_numbers))
not_sum_of_two_abundants = set()


def is_sum_of_abundants(number):
    if number < 24:
        return False

    for n in range(number):
        if sorted_abundant_numbers[n] > number:
            break

        if number - sorted_abundant_numbers[n] in abundant_numbers:
            return True

    return False


for j in range(1, 28123):
    if not is_sum_of_abundants(j):
        not_sum_of_two_abundants.add(j)

print(not_sum_of_two_abundants)
print(sum(not_sum_of_two_abundants))