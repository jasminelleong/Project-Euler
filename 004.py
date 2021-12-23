# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
def is_palindrome(num) :   
    size = len(str(num))
    strNum = str(num)
    for i in range(int(size/2)) :
        if strNum[i] != strNum[size-i-1] :
            return False
    return True

#range of 3 dig nums : 100-999
largest = 1
for i in range (999,99, -1) :
    for k in range (999, 99,-1) :
        if is_palindrome(i*k):
            if i* k > largest :
                largest = i * k
print(largest)