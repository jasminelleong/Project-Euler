# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#     13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
# proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
def find_biggest_chain_under(max) :
    big_chain_start_val = 1
    bigchain = 1
    for num in range(max, 100, -1) :
        count = 1
        startingnum = num
        while num != 1 :
            count +=1
            if num % 2 == 0 :
                num = int(num/2)
            else :
                num = int(num *3) +1
        if count > bigchain :
            print (startingnum, 'is the num', 'count is:', count)
            big_chain_start_val = startingnum
            bigchain = count
    return big_chain_start_val
print(find_biggest_chain_under(1000000))

