# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import math
prime_nums = []
prime_nums.append(2)
def isPrime(n) :
    if n == 2 :
        return True
    for i in range(2, int(math.sqrt((n))+1)) :
        if n % i == 0:
            return False

    #print(factors)
    return True
    
num = 3
while len(prime_nums) < 10001 :
    if isPrime(num) :
        prime_nums.append(num)
    num += 2
print(sorted(prime_nums)[-1])
print (prime_nums[0:100])