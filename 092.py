# A number chain is created by continuously adding the square of the digits in a number to form a new number until it
# has been seen before.
#
# For example,
#
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that
# EVERY starting number will eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?


def next_in_chain(num: int) -> int:
    str_num = str(num)
    return sum([int(digit) * int(digit) for digit in str_num])


num_arriving_at_89 = 0

for i in range(1, 10000000):
    chain_num = i
    while chain_num != 1 and chain_num != 89:
        chain_num = next_in_chain(chain_num)

    if chain_num == 89:
        num_arriving_at_89 += 1


print(num_arriving_at_89)
