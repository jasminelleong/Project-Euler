# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
from utilities import is_prime
import math
# start with 2 then we can check only odd numbers
sum = 2
for i in range(1, 2000000, 2) :
    if is_prime(i) :
        sum += i
print (sum)