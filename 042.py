# The nth term of the sequence of triangle numbers is given by, t(n) = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
# we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
# triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
# English words, how many are triangle words?
from utilities import get_word_score, is_triangle_number

words_string = ''

with open('042_words.txt') as file:
    words_string = file.read()

words = words_string.split('"')
filtered_words = []
for word in words:
    if word == '' or word == ',':
        continue
    filtered_words.append(word)


triangle_word_count = 0

for word in filtered_words:
    word_score = get_word_score(word)
    if is_triangle_number(word_score):
        triangle_word_count += 1

print(triangle_word_count)