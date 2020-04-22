# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)
from utilities import is_palindrome, to_binary_string

cumulative_sum = 0

for i in range(1000000):
    if is_palindrome(i):
        if is_palindrome(to_binary_string(i)):
            cumulative_sum += i

print(cumulative_sum)
