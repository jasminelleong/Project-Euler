# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated
# product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
# which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
# with (1,2, ... , n) where n > 1?

from utilities import all_string_permutations


def is_concatenated_product(pandigital: str) -> bool:
    for i in range(1, 5):
        first_product = pandigital[:i]
        remaining_pandigital = pandigital[i:]
        next_multiplier = 2
        while remaining_pandigital != 0:
            next_product = int(first_product) * next_multiplier
            if not remaining_pandigital.startswith(str(next_product)):
                break

            remaining_pandigital = pandigital[i + len(str(next_product)):]
            next_multiplier += 1

        if remaining_pandigital == '':
            return True

    return False


all_one_through_nine_pandigitals = reversed(sorted(all_string_permutations('987654321')))

for pandigital in all_one_through_nine_pandigitals:
    if is_concatenated_product(pandigital):
        print(pandigital)
        exit(0)

