# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def evenly_divisible_1_through_20(number):
    if number % 1 == 0 \
            and number % 2 == 0 \
            and number % 4 == 0 \
            and number % 5 == 0 \
            and number % 6 == 0 \
            and number % 7 == 0 \
            and number % 8 == 0 \
            and number % 9 == 0 \
            and number % 10 == 0 \
            and number % 11 == 0 \
            and number % 12 == 0 \
            and number % 13 == 0 \
            and number % 14 == 0 \
            and number % 15 == 0 \
            and number % 16 == 0 \
            and number % 17 == 0 \
            and number % 18 == 0 \
            and number % 19 == 0 \
            and number % 20 == 0:
        return True
    return False


i = 1

while True:
    if evenly_divisible_1_through_20(i):
        print(i)
        exit(0)
    i += 1
