from datetime import datetime
from copy import copy

user_input = input("Enter your birthdate (DD.MM.YYYY): ")
try:
    birthdate = datetime.strptime(user_input, "%d.%m.%Y")
except ValueError:
    print("The entered value is not a valid date or not of the format DD.MM.YYYY")

# the input is valid, so let's calculate the remaining time now
now = datetime.now()

next_birthday = copy(birthdate).replace(year=now.year)
if (next_birthday < now):
    next_birthday = next_birthday.replace(year=now.year + 1)

age = next_birthday.year - birthdate.year

time_till_next_birthday = next_birthday - now
time_till_next_birthday.seconds
hours = int(time_till_next_birthday.seconds / 3600)
minutes = int((time_till_next_birthday.seconds - (hours * 3600)) / 60)

print(f"The time remaining until your {age}th birthday is {time_till_next_birthday.days} days, {hours} hours and {minutes} minutes.")
