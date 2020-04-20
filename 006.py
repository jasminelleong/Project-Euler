# The sum of the squares of the first ten natural numbers is,
# 1^2+2^2+...+10^2=385
#
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025−385=2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

naturals = [i for i in range(1, 101)]
squares = [i*i for i in naturals]

naturals_sum = sum(naturals)
square_of_sum = naturals_sum * naturals_sum
sum_of_squares = sum(squares)
difference = square_of_sum - sum_of_squares
print(difference)
