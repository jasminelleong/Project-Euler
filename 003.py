# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

def isPrime(n) :
    foundFactor = False
    if n % 2 == 0 :
        return False
    for i in range(1, int(math.sqrt((n)+1))) :
        if n % i == 0:
            if i != 1 :
                foundFactor = True

    #print(factors)
    if foundFactor == False:
        return True
    else :
        return False


def largestPrimeFactor(n) :
    #factors = []
    for i in reversed(range(1, int(math.sqrt(n)))) :
        if i % 2 != 0 :
            if n % i == 0 :
                if isPrime(i) :
                    return i
    
    return 1

print (largestPrimeFactor(600851475143))
#print (isPrime(35))