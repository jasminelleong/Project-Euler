# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly
# 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
from itertools import permutations

string = 'ddddddddddddddddddddrrrrrrrrrrrrrrrrrrrr'
lst = ['r','r','d','d']
perms =  permutations(string)
print(len(set(perms)))
# this doesnt actually work
