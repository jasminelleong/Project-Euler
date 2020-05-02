# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total
# from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text
# file containing a triangle with one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this
# problem, as there are 2^99 altogether! If you could check one trillion (10^12) routes every second it would take over
# twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

from typing import List

triangle_rows = open('067_triangle.txt', 'r').readlines()

main_triangle = []

for row in triangle_rows:
    main_triangle.append([int(num) for num in row.split(' ')])


class Triangle(object):
    def __init__(self, triangle):
        self.triangle: List[List[int]] = triangle

    def get_sub_triangle(self, row, col):
        sub_triangle = []
        for r in range(row, len(self.triangle)):
            sub_triangle.append(self.triangle[r][col:r + col])
        return Triangle(sub_triangle)

    def left_path_sum(self):
        return sum([row[0] for row in self.triangle])

    def right_path_sum(self):
        return sum([row[-1] for row in self.triangle])

    def coalesce_lower_row(self, row_num):
        lower_row = self.triangle[row_num + 1]
        for col_num in range(len(self.triangle[row_num])):
            if lower_row[col_num] > lower_row[col_num + 1]:
                self.triangle[row_num][col_num] += lower_row[col_num]
            else:
                self.triangle[row_num][col_num] += lower_row[col_num + 1]


tri = Triangle(main_triangle)

for r in range(len(tri.triangle) - 2, -1, -1):
    tri.coalesce_lower_row(r)

print(tri.triangle[0][0])