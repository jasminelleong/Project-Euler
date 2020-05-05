# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general
# circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?


def get_num_combinations(coin_num, total_value, coins_count=None):
    if coin_num == 0:
        # print([total_value] + coins_count)
        return 1

    if coins_count is None:
        coins_count = []

    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    coin_value = coins[coin_num]
    max_coins = total_value // coin_value
    num_combinations = 0

    for num_coins in range(max_coins + 1):
        remaining_value = total_value - (num_coins * coin_value)
        if remaining_value == 0:
            num_combinations += 1
        else:
            num_combinations += get_num_combinations(coin_num - 1, remaining_value, [num_coins] + coins_count)

    return num_combinations


print(get_num_combinations(7, 200))
