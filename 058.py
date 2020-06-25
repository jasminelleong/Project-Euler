# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
#
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is
# that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
#
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If
# this process is continued, what is the side length of the square spiral for which the ratio of primes along both
# diagonals first falls below 10%?
from utilities import is_prime


def generate_next_spiral_corners(side_length, last_value):
    corner_delta = side_length - 1
    first_corner = last_value + corner_delta
    return [first_corner, first_corner + corner_delta, first_corner + corner_delta * 2, first_corner + corner_delta * 3]


current_side_length = 1
spiral_corners = [1]
diagonal_prime_saturation_pct = 100
current_corner_prime_amount = 0

iterations = 0

while diagonal_prime_saturation_pct >= 10:
    current_side_length += 2
    new_spiral_corners = generate_next_spiral_corners(current_side_length, spiral_corners[-1])
    spiral_corners += new_spiral_corners
    new_diagonal_primes = [corner for corner in new_spiral_corners if is_prime(corner)]
    current_corner_prime_amount += len(new_diagonal_primes)
    diagonal_prime_saturation_pct = current_corner_prime_amount / len(spiral_corners) * 100

    iterations += 1
    if iterations % 100 == 0:
        print('Prime saturation: {}%'.format(diagonal_prime_saturation_pct))

print('Prime saturation: {}%'.format(diagonal_prime_saturation_pct))
print('Side length: {}'.format(current_side_length))
