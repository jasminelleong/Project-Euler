# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

cumulative_self_power_mod_sum = 0

for i in range(1, 1001):
    # Thank you Python
    cumulative_self_power_mod_sum += pow(i, i, 10000000000)

print(cumulative_self_power_mod_sum % 10000000000)
