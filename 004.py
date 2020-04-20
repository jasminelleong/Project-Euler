# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
from utilities import is_palindrome

products = []

for x in range(100, 1000):
    for y in range(100, 1000):
        products.append(x * y)

products.sort()
products = reversed(products)

for product in products:
    if is_palindrome(product):
        print(product)
        exit(0)
