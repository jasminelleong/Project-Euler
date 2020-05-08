# It is possible to write five as a sum in exactly six different ways:
#
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written as a sum of at least two positive integers?


def count_num_combinations(total_amount, diff=0, sum_series=[]):
    if total_amount - diff == 0:
        if len(sum_series) > 1:
            # print(sum_series)
            return 1
        else:
            return 0

    remaining_total = total_amount - diff
    if remaining_total < diff:
        return 0
    combo_count = 0

    if diff == 0:
        iterate_start = 1
    else:
        iterate_start = diff

    for i in range(iterate_start, remaining_total + 1):
        combo_count += count_num_combinations(remaining_total, i, [i] + sum_series)

    return combo_count


print(count_num_combinations(100))

