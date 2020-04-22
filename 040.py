# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

big_champernowne_string = ''

for i in range(1, 200000):
    big_champernowne_string += str(i)

digits_of_interest = [
    big_champernowne_string[0],
    big_champernowne_string[9],
    big_champernowne_string[99],
    big_champernowne_string[999],
    big_champernowne_string[9999],
    big_champernowne_string[99999],
    big_champernowne_string[999999]
]

digit_product = 1

for digit in digits_of_interest:
    digit_product *= int(digit)

print(digit_product)
