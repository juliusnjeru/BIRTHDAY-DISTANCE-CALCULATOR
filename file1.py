#!

import time
from datetime import datetime, date

# from typing import Any

today = date.today()
# print(today == date.fromtimestamp(time.time()))

# print(today)
month = int(input("Your Birth Month: "))
day = int(input("Your Birth Day: "))

my_birthday = date(today.year, month, day)

if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
    print(f"It will be next year on {my_birthday}")

# print(my_birthday)

time_to_myBirthDay = abs(my_birthday - today)
# print(time_to_myBirthDay)

print(f'{time_to_myBirthDay.days} days to your birthday!')
time.sleep(5)
