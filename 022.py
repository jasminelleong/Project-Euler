# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first
# names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?


def get_letter_score(letter):
    return ord(letter) - 64


def get_word_score(word):
    cumulative_score = 0
    for letter in word:
        cumulative_score += get_letter_score(letter)
    return cumulative_score


names_string = ""

with open('022_names.txt') as file:
    names_string = file.read()

names = names_string.split('"')
filtered_names = []
for name in names:
    if name == '' or name == ',':
        continue
    filtered_names.append(name)

filtered_names = sorted(filtered_names)
cumulative_name_score = 0

for i in range(len(filtered_names)):
    if filtered_names[i] == 'COLIN':
        print(i)
    cumulative_name_score += get_word_score(filtered_names[i]) * (i + 1)

print(cumulative_name_score)
