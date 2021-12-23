# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#     a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

a = 0
b = 0
c = 335
#1000 - c %2 != 0 because if its divisible by 2, then a !< b
def generateTriplet(num) :
    a = 0
    b = 0
    for i in range(501, 1, -2):
        rest = num - i
        if rest % 2 != 0 :
            for b in range (rest-1, 11, -1) :
                a = rest - b
                if i > b and b > a and a + b + i ==1000:
                    if a**2 + b**2 == i**2 :
                        print ('a:', a, 'b', b, 'c', i)
                        print ('a^2 + b^2 = ', a**2+b**2, 'and c^2=', i**2)
generateTriplet(1000)