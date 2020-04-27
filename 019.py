# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
jan_1_1900 = 0
day = jan_1_1900
sundays_on_first = 0

for year in range(1900, 2001):
    for month in month_days:
        if year >= 1901 and day % 7 == 6:
            sundays_on_first += 1
        if month == 28:
            if (year % 100 == 0 and year % 400 == 0) or year % 4 == 0:
                day += 29
        else:
            day += month

print(sundays_on_first)
