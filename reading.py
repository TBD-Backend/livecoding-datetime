from datetime import datetime

date = "March 28 2011, 16:12"

# convert to datetime object

converted_date = datetime.strptime(date, "%B %d %Y, %H:%M")

print(converted_date.year)
print(converted_date.hour)