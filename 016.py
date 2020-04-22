# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
import math

# Thank you Python
big_int_string = str(int(math.pow(2, 1000)))
digit_sum = 0
for digit in big_int_string:
    digit_sum += int(digit)

print(digit_sum)
