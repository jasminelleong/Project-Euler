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

def isLeapYear (year) :
    #divisible by 4, not a century. The only century is 2000
    if year % 4 == 0 and year < 2000:
        return True
    return False
def numDaysinMonth (month, year) :
    if month == 9 or month == 4 or month == 6 or month == 11 :
        return 30
    if month == 2 :
        if isLeapYear(year):
            return 29
        else :
            return 28
    else :
        return 31

sundayDay = 6
sundayCount = 0


for year in range (1901, 2001) :
    for month in range (1, 13) :
        numDays = numDaysinMonth(month, year)
        while sundayDay <= numDays :
            if sundayDay == 1 :
                sundayCount += 1
            sundayDay += 7
        
        sundayDay = sundayDay - numDays
        

print(sundayCount)



# 1 january monday, 2 T 3 W 4 TH 5 Fri 6 Sat
# 7 January 1900 == sunday, 1/7, 1/14, 1/21, 1/28
# 31-28 = 3 days. 1/29 M, 1/30 T, 1/31 W. 2/1 Th 2/2 F, 2/3 S, 2/4 == sun. 7 - (Month day # (30/31) - last sunday) == next sunday
# 2/4, 2/ 11, 2/18, 2/ 25 
# 26 M 27 T 28 W 1 T 2 F 3 S 4 S
# 1900 is a leap year since it's divisible by 4 but not by 400