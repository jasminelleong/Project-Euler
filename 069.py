# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less
# than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
# prime to nine, φ(9)=6.
#
# n 	Relatively Prime 	φ(n) 	n/φ(n)
# 2 	1 	                1 	    2
# 3 	1,2 	            2 	    1.5
# 4 	1,3 	            2 	    2
# 5 	1,2,3,4 	        4 	    1.25
# 6 	1,5 	            2 	    3
# 7 	1,2,3,4,5,6 	    6 	    1.1666...
# 8 	1,3,5,7 	        4 	    2
# 9 	1,2,4,5,7,8 	    6 	    1.5
# 10 	1,3,7,9 	        4 	    2.5
#
# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
#
# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
from utilities import greatest_common_divisor

max_n_over_phi_n = 0
answer_n = 0

# I originally tried the brute-force way, but found there didn't seem to be any way to do it in a reasonable time.
# After some investigation, I noticed what we're optimizing for is numbers with a lot of prime factors.
# That naturally leads to the hypothesis: What about the number under 1 million with the most possible prime factors?
# And that lead to the right answer!

test_values = [
    2*3*5*7*11*13*17
]

for value in test_values:
    n = value
    num_relatively_prime = 0
    for j in range(1, n + 1):
        if greatest_common_divisor(n, j) == 1:
            num_relatively_prime += 1
    n_over_phi_n = n / num_relatively_prime
    print(n_over_phi_n, n)
    if n_over_phi_n > max_n_over_phi_n:
        max_n_over_phi_n = n_over_phi_n
        answer_n = n

print(max_n_over_phi_n)
