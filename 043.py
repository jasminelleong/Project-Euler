# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some
# order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.
from utilities import all_string_permutations

pandigital_strings = all_string_permutations(1234567890)
pandigital_strings = [string for string in pandigital_strings if int(string) > 1000000000]

interesting_pandigitals = []

for pandigital in pandigital_strings:
    expected_divisibility_values = [2, 3, 5, 7, 11, 13, 17]
    candidate_passes = True
    for i in range(7):
        if not int(pandigital[i + 1: i + 4]) % expected_divisibility_values[i] == 0:
            candidate_passes = False
            break

    if candidate_passes:
        print('Found interesting pandigital: {}'.format(pandigital))
        interesting_pandigitals.append(int(pandigital))

print('Interesting pandigital sum: {}'.format(sum(interesting_pandigitals)))
