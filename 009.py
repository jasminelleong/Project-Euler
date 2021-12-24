# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#     a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

a = 0
b = 0
#1000 - c %2 != 0 because if its divisible by 2, then a !< b
def generateTriplet(num) :
    a = 0
    b = 0
    for c in range(501, 1, -1):
        rest = num - c
        for b in range (rest-1, 11, -1) :
            a = rest - b
            if c > b and b > a and a + b + c ==1000:
                if a**2 + b**2 == c**2 :
                    return a * b * c
print(generateTriplet(1000))