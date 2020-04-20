import math


def fibonacci_sequence():
    second_previous_value = 1
    previous_value = 2
    yield second_previous_value
    yield previous_value
    while True:
        next_value = second_previous_value + previous_value
        second_previous_value = previous_value
        previous_value = next_value
        yield next_value


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(2, num):
        if i*i > num:
            break
        if num % i == 0:
            return False

    return True


def is_palindrome(num):
    str_version = str(num)
    num_digits_to_check = len(str_version) // 2
    for i in range(0, num_digits_to_check + 1):
        if str_version[i] != str_version[(i + 1) * -1]:
            return False

    return True
