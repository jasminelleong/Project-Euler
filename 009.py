# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#     a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

sum_to_1000_triplets = []

for a in range(1, 1000):
    for b in range(2, 1000):
        if b <= a:
            continue
        c = 1000 - b - a
        if c <= b:
            break
        sum_to_1000_triplets.append((a, b, c))

for triplet in sum_to_1000_triplets:
    a, b, c = triplet
    if a*a + b*b == c*c:
        print(triplet)
        product = a * b * c
        print(product)
