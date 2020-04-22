# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly
# 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

#

# Answer:

# To get from the top-left to the bottom-right of a 2x2 grid, we must make exactly 4 decisions, and the number of
# "right moves" must equal the number of "down moves". This can be represented by a binary list:
# [0, 0, 1, 1]
# [1, 0, 1, 0]

# All such 4-decision sequences are valid except those with an unequal number of right and left turns:
# [0, 0, 0, 1] <-- invalid

# For a 2x2 grid, there are 10 such invalid decision lists:
# [0, 0, 0, 1]
# [0, 0, 1, 0]
# [0, 1, 0, 0]
# [1, 0, 0, 0]
# [0, 1, 1, 1]
# [1, 0, 1, 1]
# [1, 1, 0, 1]
# [1, 1, 1, 0]
# [1, 1, 1, 1]
# [0, 0, 0, 0]

# So the number of valid paths is 2^4 - 10.

# Generally, for a square grid, there are '2n choose n' valid paths.

# So, for a 20x20 grid, the answer is:
# 40! / (20! * 20!)
# Or 137846528820.
