#
#
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
# Find the maximum total from top to bottom of the triangle below:
#
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However,
# Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force,
# and requires a clever method! ;o)
from typing import List

str_triangle = \
    """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

main_triangle = []

triangle_rows = str_triangle.split('\n')

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
