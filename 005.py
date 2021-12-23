# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

num = 252000

def smallestEvenlyDivisbleNum (max) :
    num = 2520
    while num <= 23279256009 :
        for i in reversed(range(1, max+1)) :
            if num % i != 0 :
             #print ('not this one')
             
                 break
            if i == 1 :
                print(num, 'is it!')
                return num
        num +=20
print(smallestEvenlyDivisbleNum(20))