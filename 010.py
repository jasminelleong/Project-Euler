# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
from utilities import all_prime_numbers

primes_below_2_mil = []
prime_generator = all_prime_numbers()

for prime in prime_generator:
    if prime >= 2000000:
        prime_generator.close()
    else:
        primes_below_2_mil.append(prime)

sum_of_primes = sum(primes_below_2_mil)
print(sum_of_primes)
