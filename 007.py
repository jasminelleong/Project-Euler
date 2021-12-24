# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
from utilities import is_prime
import math
prime_nums = []
# Since 2 is only even number, we'll add this so we can only check odd numbers after that
prime_nums.append(2)
num = 3
while len(prime_nums) < 10001 :
    if is_prime(num) :
        prime_nums.append(num)
    num += 2
print(sorted(prime_nums)[-1])