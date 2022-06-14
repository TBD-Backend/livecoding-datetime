from datetime import datetime, date

# get current date and time
print(datetime.today())

# get current date
print(date.today())

date_as_string = "2022-01-26"

print(date.fromisoformat(date_as_string))

# Create some datetime objects

# Create a datetime object with time
date_1 = datetime(year=2022, month=1, day=26, hour=10, minute=30, second=59)

print(date_1)

# Create a datetime object with just the date
date_2 = date(year=2022, month=1, day=26)

print(date_2)
