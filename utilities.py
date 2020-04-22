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


def triangle_numbers():
    previous_iteration = 0
    cumulative_sum = 0
    while True:
        next_iteration = previous_iteration + 1
        cumulative_sum += next_iteration
        previous_iteration = next_iteration
        yield cumulative_sum


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


def all_prime_numbers():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1


def calculate_divisors(num):
    divisors = [1, num]
    square_root = int(math.sqrt(num))

    if square_root * square_root == num:
        # Num is perfect square
        divisors.append(square_root)

    for i in range(2, square_root):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num // i)

    return divisors


def collatz_step(num):
    if num % 2 == 0:
        return num // 2
    return (num * 3) + 1
