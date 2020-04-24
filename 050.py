# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
from utilities import is_prime, all_prime_numbers

primes = []
prime_generator = all_prime_numbers()

for i in range(10000):
    primes.append(next(prime_generator))

longest_streak = 0
longest_streak_prime = None

for i in range(len(primes)):
    for j in range(i, len(primes)):
        prime_sum = sum(primes[i:j])
        if prime_sum > 1000000:
            # Stop increasing the streak test length
            break
        if (j - i) > longest_streak and is_prime(prime_sum):
            longest_streak = j - i
            longest_streak_prime = sum(primes[i:j])

print('Sum of {} primes:'.format(longest_streak))
print(longest_streak_prime)
