# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


def get_spiral_corners(width):
    if width == 1:
        return [1]

    smaller_grid = get_spiral_corners(width - 2)
    largest_smaller_grid_corner = smaller_grid[-1]
    if smaller_grid[0] == 1:
        corner_distance = 2
    else:
        corner_distance = (smaller_grid[1] - smaller_grid[0]) + 2

    corners = []
    for i in range(4):
        corners.append(largest_smaller_grid_corner + corner_distance + (corner_distance * i))

    return corners


def get_spiral_corner_sum(width):
    if width == 1:
        print(get_spiral_corners(1))
        return sum(get_spiral_corners(1))

    print(get_spiral_corners(width))
    return sum(get_spiral_corners(width)) + get_spiral_corner_sum(width - 2)


print(get_spiral_corner_sum(1001))
