# The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In
# fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.
from utilities import is_permutation

permuted_cubes = dict()
cubes_by_digit_amounts = dict()

for i in range(10000):
    cube = pow(i, 3)
    num_digits = len(str(cube))
    if num_digits not in cubes_by_digit_amounts:
        cubes_by_digit_amounts[num_digits] = {cube}
    else:
        cubes_by_digit_amounts[num_digits].add(cube)

    for other_cube in cubes_by_digit_amounts[num_digits]:
        if is_permutation(cube, other_cube):
            sorted_digits_string = ''.join(sorted(str(cube)))
            if sorted_digits_string not in permuted_cubes:
                permuted_cubes[sorted_digits_string] = [cube]
            elif cube not in permuted_cubes[sorted_digits_string]:
                permuted_cubes[sorted_digits_string].append(cube)
                if len(permuted_cubes[sorted_digits_string]) == 5:
                    print(sorted(permuted_cubes[sorted_digits_string]))
                    exit(0)
