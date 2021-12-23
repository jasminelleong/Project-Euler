# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
import math
def isPrime(n) :
    if n == 2 :
        return True
    if n ==1 :
        return False
    for i in range(2, int(math.sqrt((n))+1)) :
        if n % i == 0:
            return False
    return True
sum = 2
for i in range(1, 2000000, 2) :
    if isPrime(i) :
        sum += i
print (sum)