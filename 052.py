# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different
# order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

from utilities import is_permutation

for i in range(100000, 100000000):
    if is_permutation(2 * i, i) \
            and is_permutation(3 * i, i) \
            and is_permutation(4 * i, i) \
            and is_permutation(5 * i, i) \
            and is_permutation(6 * i, i):
        print(i)
        exit(0)
