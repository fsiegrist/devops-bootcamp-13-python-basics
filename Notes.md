## Notes on the videos for Module 13 "Programming Basics with Python"
<br />

<details>
<summary>Video: 1 - Introduction to Python</summary>
<br />

### What Python is used for?
- Web Development: django, Flask
- Data Science, Machine Learning, Artificial Intelligence: NumPy, Pandas, Matplotlib, SciPi, SciKit-Learn, TensorFlow, Keras, Seaborn, PyTorch, Theano
- Web Scraping
- Automation: Automate DevOps tasks and general tasks: modules for CI/CD, AWS, Google Cloud, monitoring or working with Excel sheets

### DevOps tasks to automate with Python
- System Health Checks
- Monitoring Tasks
- Backup Tasks
- Custom Ansible Modules
- Data Visualization
- Managing Cron
- CI/CD related Tasks (update Jira ticket after Jenkins build, trigger Jenkins job on specific events, send notifications to team members on specific events)
- Cleanup Tasks (e.g. remove old Docker images)

</details>

*****

<details>
<summary>Video: 2 - Installation and Local Setup</summary>
<br />

### Install Python
Visit the [Python Download Page](https://www.python.org/downloads/) and download the installer for your OS. Install Python using this installer. Or install Python using homebrew:

```sh
brew update

# install latest python3
brew install python

# or (using PyEnv, a tool allowing to have multiple python versions installed)
brew install pyenv
pyenv install 3.11.4

# check the version
python3 --version
# Python 3.11.4
```

### Setup PyCharm IDE
Download the PyCharm installer for your OS from the [PyCharm Download Page](https://www.jetbrains.com/pycharm/download/) and install it. Or if you have the [JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/) installed, install PyCharm from there.

Open PyCharm and press the "New Project" button. Adjust the project name at the end of the "Location" string (or the whole "Location" string if you want the project to be located somewhere else). If you installed Python using the installer downloaded from the python download page, the "Base interpreter" will be '/usr/local/bin/python3.11'. If you installed python using homebrew, it will be '/opt/homebrew/bin/python3.11'. Executing `which python3` will help.

Press the "Create" button and once the editor has opened remove all the content from `main.py`.

### Links
- [Python Home](https://www.python.org/)
- [Documentation](https://docs.python.org/3.11/index.html)
- [Beginner's Tutorial](https://docs.python.org/3.11/tutorial/)
- [Python Central](https://www.pythoncentral.io/)

</details>

*****

<details>
<summary>Videos 5 - 16</summary>
<br />

### 5 - Strings and Number Data Types
- String literals can be written in single quotes or double quotes. Their data type is `str`.
- Numbers are of type `int` or `float`.

#### String concatenation
```python
print("20 days are " + str(20 * 24 * 60) + " minutes.")
print(f"20 days are {20 * 24 * 60} minutes.")
```

### 6 - Variables
Python is dynamically typed, so there's no need to define the type of a variable. The naming convention for variables is lowercase with underscore as word delimiter:

```python
number_of_seconds_per_day = 24 * 60 * 60
time_unit = "seconds"
```

### 7 - Functions
```python
# defining a function
def days_to_units(number_of_days, unit_name, number_of_units_per_day):
    return f"{number_of_days} days are {number_of_days * number_of_units_per_day} {unit_name}."

# calling a function
seconds_in_20_days = days_to_units(20, "seconds", 24 * 60 * 60)
print(days_to_units(35, "minutes", 24 * 60))
```

### 8 - Accepting User Input
```python
num_of_days = input("Number of days:\n")

# num_of_days is of type string; int(num_of_days) casts it to a number
print(days_to_units(int(num_of_days), "minutes", 24 * 60))
```

### 9 - Conditionals (if / else) and Boolean Data Type
```python
if x > y:
    print("x > y")
elif x == y:
    print("x == y")
else:
    print("x < y")

print(type(x > y))
# => <class 'bool'>

# bool literals
True
False
```

### 10 - Error Handling with Try-Except
```python
try:
    value = int("11x")
    print(value)
except Exception as ex:
    print(type(ex))     # <class 'ValueError'>
    print(ex)           # invalid literal for int() with base 10: '11x'

try:
    1/0
except ZeroDivisionError as err:
    print(err)          # division by zero

try:
    value = int(input("enter a value > 0: "))
    if (value <= 0):
        raise Exception("The value must be greater than zero.")
    print(value)
except ValueError as err:
    print(err)
except Exception as ex:
    print(ex)
```

### 11 - While Loops
```python
while True:
    user_input = input("Enter a value: ")
    if (user_input == "exit"):
        break
    print("You entered {user_input}.")
```

### 12 - Lists and For Loops
```python
# list literal
[1, 5, 7, 2, 5]
["foo", "bar", "hello", "world"]

# for loop over a list
for element in [1, True, "foo", 3.141592654]:
    print(element)

user_input = input("Enter a comma separated list of values: ") # 1, True, "foo", 3.141592654
input_as_list = user_input.split(", ")
print(type(user_input)) # <class 'str'>
print(type(input_as_list)) # <class 'list'>
print(input_as_list) # ['1', 'True', '"foo"', '3.141592654']

for element in input_as_list:
    print(element)

seasons = ["spring", "summer", "fall", "winter"]
print(seasons[0]) # spring
print(seasons[4]) # => IndexError: list index out of range

seasons.append("the fifth element")
print(seasons[4]) # the fifth element
seasons.remove("the fifth element")

my_list = [1,2,3,2,1]
my_list.remove(2) # [1,3,2,1] -> remove the first occurrance of the given element
```

### 13 - Comments
```python
# line comment
"""
this is
a multiline
comment
it's actually a multiline string but since it isn't assigned to a variable or printed out,
it has just no side effect
"""
```

### 14 - Sets
Sets contain no duplicates and the elements have no order.

```python
my_list = [1,2,3,2,1]
my_set = set(my_list)
print(my_set) # {1, 2, 3}
print(type(my_set)) # <class 'set'>

seasons = {"spring", "summer", "fall", "winter"}
for element in seasons:
    print(element)

seasons.add("the fifth element")
seasons.remove("the fifth element")
```

### 15 - Build-In Functions
Examples:
- print("message")
- input("Enter a value: ")
- set([1, 2, 3])
- int("10")
- "1 2 3".split()
- [1, 3, 7].count()

[Built-In Functions](https://docs.python.org/3.11/library/functions.html)

### 16 - Dictionary Data Type 
```python
my_dictionary = {
    "days": 20,
    "unit": "hours"
}
print(my_dictionary["days"])
print(type(my_dictionary)) # <class 'dict'>
```

</details>

*****

<details>
<summary>Video: 17 - Modules</summary>
<br />


A module allows you to logically organize your Python code, so it should contain related code. A module is just a normal Python file (`*.py`). The file name without the extension is the module name. To use a module in another file, it has to be imported.

_main1.py_
```python
import helper # imports the whole module (all functions and variables)
import subdir.utilities as util # import a module and use it with another name


number = input(helper.prompt)         # use the variable defined in the module
result = helper.do_some_stuff(number) # call the function on the module
print(result)

print(util.remove_leading_and_trailing_blanks("   text  "))
```

_main2.py_
```python
from helper import prompt, do_some_stuff # imports only prompt and do_some_stuff()
from subdir.utilites import remove_leading_and_trailing_blanks as trim
# or: from helper import *                 imports everything

number = input(prompt)         # no need to specify the module here
result = do_some_stuff(number) # no need to specify the module here
print(result)

print(trim("   text  "))
```

_helper.py_
```python
prompt = "Enter a number: "

def do_some_stuff(number):
    ...
    return result

def some_other_function():
    ...
```

_subdir/utilities.py_
```python
def remove_leading_and_trailing_blanks(value):
    ...
```

You can also use existing modules. Python comes with a set of [built-in modules](https://docs.python.org/3/py-modindex.html).

```python
import logging

logger = logging.getLogger("MAIN")
logger.error("An error occurred")
```

But there are many more available, which are NOT part of the Python installation. You need to install these third-party packages (see notes on video 19).

</details>

*****