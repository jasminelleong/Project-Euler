import math
from typing import List


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


def is_palindrome(value: int or str):
    str_version = str(value)
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

    for i in range(2, square_root + 1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num // i)

    return list(set(divisors))


def collatz_step(num):
    if num % 2 == 0:
        return num // 2
    return (num * 3) + 1


def integer_to_words(number):
    def digit_to_word(digit):
        if digit == 0:
            return ""
        if digit == 1:
            return "one"
        if digit == 2:
            return "two"
        if digit == 3:
            return "three"
        if digit == 4:
            return "four"
        if digit == 5:
            return "five"
        if digit == 6:
            return "six"
        if digit == 7:
            return "seven"
        if digit == 8:
            return "eight"
        if digit == 9:
            return "nine"

    if number == 1000:
        return "one thousand"
    if number >= 100:
        partial_answer = digit_to_word(number // 100) + ' hundred '
        if number % 100 != 0:
            partial_answer += 'and '
            return partial_answer + integer_to_words(number % 100)

    if number >= 20:
        if number <= 29:
            partial_answer = "twenty"
        elif number <= 39:
            partial_answer = "thirty"
        elif number <= 49:
            partial_answer = "forty"
        elif number <= 59:
            partial_answer = "fifty"
        elif number <= 69:
            partial_answer = "sixty"
        elif number <= 79:
            partial_answer = "seventy"
        elif number <= 89:
            partial_answer = "eighty"
        elif number <= 99:
            partial_answer = "ninety"

        if number % 10 != 0:
            partial_answer += '-' + digit_to_word(number % 10)

        return partial_answer

    if number < 10:
        return digit_to_word(number)

    if number == 10:
        return "ten"
    if number == 11:
        return "eleven"
    if number == 12:
        return "twelve"
    if number == 13:
        return "thirteen"
    if number == 14:
        return "fourteen"
    if number == 15:
        return "fifteen"
    if number == 16:
        return "sixteen"
    if number == 17:
        return "seventeen"
    if number == 18:
        return "eighteen"
    if number == 19:
        return "nineteen"


def get_proper_divisors(number):
    divisors = calculate_divisors(number)
    divisors.remove(number)
    return divisors


def solve_quadratic(a, b, n):
    return math.pow(n, 2) + (a * n) + b


def to_binary_string(num: int) -> str:
    reverse_binary_string = ''
    if num == 0:
        return '0'
    while num > 0:
        reverse_binary_string += str(num % 2)
        num = num // 2
    return reverse_binary_string[::-1]


def generate_rotations(num: int) -> List[int]:
    rotations = []
    string_num = str(num)
    for i in range(len(string_num)):
        rotations.append(int(string_num[i:] + string_num[:i]))
    return rotations


def is_triangle_number(num: int) -> bool:
    doubled_num = num * 2
    truncated_square_root = int(math.sqrt(doubled_num))
    if doubled_num / truncated_square_root == (truncated_square_root + 1):
        return True
    return False


def is_pentagonal(num: int) -> bool:
    # O(1)
    # Inverse pentagonal number function
    pentagonal_index = (1 + math.sqrt(1 + 24 * num)) / 6
    return pentagonal_index.is_integer()


def is_hexagonal(num: int) -> bool:
    # O(1)
    # Inverse hexagonal formula
    hexagonal_index = (1 + math.sqrt(1 + 8 * num))
    return hexagonal_index.is_integer()


def get_letter_score(letter):
    return ord(letter) - 64


def get_word_score(word):
    cumulative_score = 0
    for letter in word:
        cumulative_score += get_letter_score(letter)
    return cumulative_score
