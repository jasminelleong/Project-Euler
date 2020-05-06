# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
#
# 1! + 4! + 5! = 1 + 24 + 120 = 145
#
# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns
# out that there are only three such loops that exist:
#
# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872
#
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
#
# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)
#
# Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting
# number below one million is sixty terms.
#
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
import math


def next_in_factorial_digit_sum_chain(num: int) -> int:
    next_num = sum([math.factorial(int(digit)) for digit in str(num)])
    return next_num


contains_60_terms = 0

for i in range(1, 1000000):
    if i % 100 == 0:
        print(i)
    chain_length = 1
    chain_num = i
    seen_nums = set()
    while True:
        chain_num = next_in_factorial_digit_sum_chain(chain_num)
        if chain_num in seen_nums or chain_length > 60:
            break
        seen_nums.add(chain_num)
        chain_length += 1

    if chain_length == 60:
        contains_60_terms += 1

print(contains_60_terms)
