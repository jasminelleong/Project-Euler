# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from utilities import prime_factorization_with_powers

divisors = list(range(1, 21))
common_factors_of_divisors = dict()

for divisor in divisors:
    factorization = prime_factorization_with_powers(divisor)
    for factor in factorization.keys():
        # Only replace this divisor's factor in the common set if its power is greater
        if factor not in common_factors_of_divisors or \
                factor in common_factors_of_divisors and factorization[factor] > common_factors_of_divisors[factor]:
            common_factors_of_divisors[factor] = factorization[factor]

common_product = 1
for factor in common_factors_of_divisors.keys():
    common_product *= pow(factor, common_factors_of_divisors[factor])

print(common_product)
