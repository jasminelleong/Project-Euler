# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?

num_n_digit_n_powers = 0

for b in range(1, 100):
    for e in range(100):
        if len(str(pow(b, e))) == e:
            num_n_digit_n_powers += 1
            print('{}^{} = {}'.format(b, e, pow(b, e)))


print(num_n_digit_n_powers)
