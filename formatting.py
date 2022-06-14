from datetime import datetime

date = "January 1, 2005"
date_2 = "2007, 1 January"

# type datetime

# %B = Full month
# %d = numerical date
# %Y = Full year

# converting string to datetimeobject
converted_date = datetime.strptime(date, "%B %d, %Y")
converted_date_2 = datetime.strptime(date_2, "%Y, %d %B")

print(converted_date)
print(converted_date_2)

# 2005-01-01 00:00:00

# changing the formatting of the object
# useful for cherrypicking specific parts of the datetime object
output = converted_date.strftime("%H : %M")

print(output)