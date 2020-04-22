# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#     13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
# proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
from utilities import collatz_step

longest_chain_number = None
longest_chain_length = 0

for i in range(2, 1000000):
    starting_number = i
    chain_length = 0
    while starting_number != 1:
        starting_number = collatz_step(starting_number)
        chain_length += 1

    if chain_length > longest_chain_length:
        longest_chain_length = chain_length
        longest_chain_number = i

print("Longest chain: {} steps".format(longest_chain_length))
print("Starting number: {}".format(longest_chain_number))
