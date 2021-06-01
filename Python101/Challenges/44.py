print("Challenge 44: Write a Python program to that reads a date (from 2016/1/1 to 2016/12/31) and prints the day of the date. Jan. 1, 2016, is Friday. Note that 2016 is a leap year. ")

usr_input = '8 3'
usr_input = list(map(int, usr_input.split(' ')))

week_days = ['friday', 'saturday', 'sunday','monday', 'tuesday', 'wednesday','thursday']
days_in_leap_year = [31, 29, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
days = []

x = 0
for i in range(1,sum(days_in_leap_year)+1):
    days.append(week_days[x])
    x += 1
    if x >= 7:
        x = 0

total_days_till_that_month = days_in_leap_year[:usr_input[0] -1]
specific_day = days[sum(total_days_till_that_month) + usr_input[1]-1]

print(specific_day)