from datetime import datetime

dt = datetime(year=2020, month=11, day=4, hour=14, minute=53)

print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print(dt.strftime("%y/%B/%d %I:%M:%S %p"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print(dt.strftime("Weekday: %u"))
print(dt.strftime("Day of the year: %j"))
print(dt.strftime("Week number of the year: %W"))

