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

def sum_of_squares(max) :
    sum = 0
    for i in range(1, max+1) :
        sum += i ** 2
    return sum

def square_of_sum(max) :
    sum = 0
    for i in range(1, max+1) :
        sum = sum + i
    return sum ** 2

sum = sum_of_squares(100)
square = square_of_sum(100)
print('difference is', square-sum)