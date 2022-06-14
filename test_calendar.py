import calendar
from datetime import datetime

# set first day of the week to sunday
calendar.setfirstweekday(6)

# print(calendar.firstweekday())

print(calendar.month(2022, 6))

# get datetime object and check if the year is a leap year
time_1 = datetime(day=14, month=6, year=2022, hour=9, minute=0)

print(calendar.isleap(time_1.year))
