# Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that
# 211 = 2048 < 37 = 2187.
#
# However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over
# three million digits.
#
# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a
# base/exponent pair on each line, determine which line number has the greatest numerical value.
#
# NOTE: The first two lines in the file represent the numbers in the example given above.
import math

lines = open('099_base_exp.txt', 'r').read().split('\n')
print(lines[0])

lines = [line.split(',') for line in lines]
print(lines[0])
greatest_value = 0
greatest_value_line = 0

for line_num in range(len(lines)):
    print(line_num)
    base, exponent = int(lines[line_num][0]), int(lines[line_num][1])
    candidate_digits = exponent * math.log(base, 10)
    print(candidate_digits)
    if candidate_digits > greatest_value:
        greatest_value = candidate_digits
        greatest_value_line = line_num + 1

print(greatest_value)
print(greatest_value_line)
