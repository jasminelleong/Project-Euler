# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
# incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two
# digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
from utilities import prime_factorization

base_fractions = []
curious_fractions = set()

for i in range(10, 100):
    for j in range(i + 1, 100):
        if i % 10 == j // 10 or i // 10 == j % 10:
            base_fractions.append((i, j))

for fraction in base_fractions:
    decimal = fraction[0] / fraction[1]
    numerator_digits = str(fraction[0])
    denominator_digits = str(fraction[1])
    if numerator_digits[0] in denominator_digits:
        shared_digit = numerator_digits[0]
    elif numerator_digits[1] in denominator_digits:
        shared_digit = numerator_digits[1]
    else:
        continue

    candidate_numerator = str(fraction[0]).replace(shared_digit, '')
    if candidate_numerator == '':
        candidate_numerator = int(shared_digit)
    else:
        candidate_numerator = int(candidate_numerator)
    candidate_denominator = str(fraction[1]).replace(shared_digit, '')
    if candidate_denominator == '':
        candidate_denominator = int(shared_digit)
    else:
        candidate_denominator = int(candidate_denominator)

    if candidate_denominator == 0:
        continue

    candidate = (candidate_numerator, candidate_denominator)
    if candidate[0] / candidate[1] == decimal:
        curious_fractions.add(fraction)
        print('{}/{} == {}/{}'.format(fraction[0], fraction[1], candidate[0], candidate[1]))


product_numerator = 1
product_denominator = 1

for curious_fraction in curious_fractions:
    product_numerator *= curious_fraction[0]
    product_denominator *= curious_fraction[1]


numerator_factors = prime_factorization(product_numerator)
denominator_factors = prime_factorization(product_denominator)

final_numerator_factors = []

for factor in numerator_factors:
    if factor in denominator_factors:
        denominator_factors.remove(factor)
    else:
        final_numerator_factors.append(factor)

final_numerator = 1
final_denominator = 1

for factor in final_numerator_factors:
    final_numerator *= factor

for factor in denominator_factors:
    final_denominator *= factor

print('Simplified product of curious fractions: {}/{}'.format(final_numerator, final_denominator))
