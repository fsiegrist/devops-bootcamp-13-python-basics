## Demo Project - Write Countdown Application

### Topics of the Demo Project
Write a countdown application

### Technologies Used
- Python
- PyCharm
- Git

### Project Description
Write an application that accepts a user input of a goal and a deadline (date). Print the remaining time until that deadline.


#### Solution
Let's create a file called `time-till-deadline.py` for our program.

_time-till-deadline.py_
```python
from datetime import datetime

while True:
    user_input = input("Enter your goal with a deadline (DD.MM.YYYY) separated by a colon:\n")
    input_list = user_input.split(":")

    # input validation
    if len(input_list) != 2:
        print("Your input is not of the format goal:DD.MM.YYYY")
        continue
    
    goal = input_list[0]
    deadline = input_list[1]

    try:
        deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
        if deadline_date < datetime.today():
            print("The deadline must be a date in the future.")
            continue
    except ValueError:
        print("The deadline is not a valid date or not of the format DD.MM.YYYY")
        continue

    break

# the input is valid, so let's calculate the remaining time now
today_date = datetime.today()
time_till_deadline = deadline_date - today_date

days_till_deadline = int(time_till_deadline.total_seconds() / 3600 / 24)
hours_till_deadline = int(time_till_deadline.total_seconds() / 3600)
print(f"The time remaining to reach your goal '{goal}' is {days_till_deadline} days or {hours_till_deadline} hours.")
```