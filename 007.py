# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
from utilities import all_prime_numbers

prime_generator = all_prime_numbers()
primes = []
while len(primes) < 10001:
    primes.append(next(prime_generator))

the_10001st_prime = primes[10000]
print(the_10001st_prime)