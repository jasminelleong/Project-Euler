# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three
# solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

max_solutions = 0
max_solutions_p = None

for p in range(120, 1001):
    num_solutions = 0
    for a in range(1, p):
        for b in range(1, p - a):
            c = p - a - b
            if a * a + b * b == c * c:
                num_solutions += 1

    if num_solutions > max_solutions:
        max_solutions = num_solutions
        max_solutions_p = p

print('Max solutions: {}'.format(max_solutions))
print(max_solutions_p)
