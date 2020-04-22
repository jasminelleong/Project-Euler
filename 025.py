# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
#
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
import math

from utilities import fibonacci_sequence

# Brute Force, the musical
fibonacci_generator = fibonacci_sequence()
current_fib = 1
fib_index = 1
while len(str(current_fib)) < 1000:
    current_fib = next(fibonacci_generator)
    fib_index += 1

print(current_fib)
print(fib_index)

