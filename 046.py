# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and
# twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
from utilities import all_primes_up_to

primes_under_100k = all_primes_up_to(100000)
double_squares = [i * i * 2 for i in range(1000)]
prime_and_twice_squares = set()

for prime in primes_under_100k:
    for double_square in double_squares:
        prime_and_twice_squares.add(double_square + prime)

for i in range(3, len(prime_and_twice_squares), 2):
    if i not in prime_and_twice_squares:
        print(i)
        exit(0)

