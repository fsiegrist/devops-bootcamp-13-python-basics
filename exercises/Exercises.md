## Exercises for Module 13 "Programming Basics with Python"
<br />

<details>
<summary>Exercise 1: Working with Lists</summary>
<br />

**Tasks:**

Using the following list:

```python
my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
```
1. Task: Write a program that prints out all the elements of the list that are higher than or equal 10.
2. Task: Instead of printing the elements one by one, make a new list that has all the elements higher than or equal 10 from this list in it and print out this new list.
3. Task: Ask the user for a number as input and print a list that contains only those elements from my_list that are higher than the number given by the user.

**Solution:**

1. Task
```python
for number in my_list:
    if number >= 10:
        print(number)
```

2. Task
```python
new_list = []
for number in my_list:
    if number >= 10:
        new_list.append(number)
print(new_list)
```

3. Task
```python
threshold = input("Enter a number: ")
new_list = []
for number in my_list:
    if number > int(threshold):
        new_list.append(number)
print(new_list)
```

</details>

******

<details>
<summary>Exercise 2: Working with Dictionaries</summary>
<br />

**Tasks:**

Using the following dictionary:
```python
employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}
```

Write a Python Script that:
1. Task: Updates the job to Software Engineer
2. Task: Removes the age key from the dictionary
3. Task: Loops through the dictionary and prints the key:value pairs one by one


Using the following 2 dictionaries:
```python
dict_one = {'a': 100, 'b': 400} 
dict_two = {'x': 300, 'y': 200}
```

Write a Python Script that:
4. Task: Merges these two Python dictionaries into 1 new dictionary
5. Task: Sums up all the values in the new dictionary and print it out
6. Task: Prints the max and minimum values of the dictionary

**Solution:**

1. Task
```python
employee['job'] = 'Software Engineer'
```

2. Task
```python
employee.pop('age')
```

3. Task
```python
for key, value in employee.items():
    print(f"{key}:{value}")
```

4. Task
```python
dict_merged = dict_one.copy()
dict_merged.update(dict_two)
```

5. Task
```python
sum = 0
for value in dict_merged.values():
    sum = sum + value
print(f"Sum of values = {sum}")
```

6. Task
```python
min = None
max = None
for value in dict_merged.values():
    if min == None:
        min = value
    elif value < min:
        min = value
    if max == None:
        max = value
    elif value > max:
        max = value
print(f"min = {min}, max = {max}")

# or
all_values = []
for value in dict_merged.values():
    all_values.append(value)
all_values.sort()
print(f"min = {all_values[0]}, max = {all_values[-1]}")
```

</details>

******

<details>
<summary>Exercise 3: Working with List of Dictionaries</summary>
<br />

**Tasks:**

Using a list of 2 dictionaries:
```python
employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]
```

Write a Python Program that:
1. Task: Prints out - the name, job and city of each employee using a loop. The program must work for any number of employees in the list, not just 2.
2. Task: Prints the country of the second employee in the list by accessing it directly without the loop.

**Solution:**

1. Task
```python
for employee in employees:
    print(f"Name: {employee.get('name')}")
    print(f"Job:  {employee.get('job')}")
    print(f"City: {employee.get('address').get('city')}")
    print("--------")
```

2. Task
```python
print(f"2nd employee's country: {employees[1].get('address').get('country')}")
```

</details>

******

<details>
<summary>Exercise 4: Working with Functions</summary>
<br />

**Tasks:**

1. Task: Write a function that accepts a list of dictionaries with employee age (see example list from the Exercise 3) and prints out the name and age of the youngest employee.
2. Task: Write a function that accepts a string and calculates the number of upper case letters and lower case letters.
3. Task: Write a function that prints the even numbers from a provided list.
4. Task: For cleaner code, declare these functions in its own helper module and use them in the main.py file

**Solution:**

1. Task
```python
def print_youngest(employees):
    youngest = employees[0]
    for employee in employees:
        if int(employee.get('age')) < int(youngest.get('age')):
            youngest = employee
    print(f"{youngest.get('name')} ({youngest.get('age')})")
```

2. Task
```python
def count_upper_lower_case_characters(text):
    upper = 0
    lower = 0
    for character in list(text):
        if character.isupper():
            upper += 1
        elif character.islower():
            lower += 1
    print(f"number of uppercase characters: {upper}")
    print(f"number of lowercase characters: {lower}")
```

3. Task
```python
def print_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)
```

4. Task

Move all the above functions into a file called `ex4_helper.py` and create a file called `ex4_main.py` with the following content:

```python
from ex4_helper import *

# test print_youngest():
employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tom",
  "age": 15,
  "birthday": "2005-04-06",
  "job": "Student",
  "address": {
    "city": "Zurich",
    "country": "Switzerland"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

print_youngest(employees) # should print "Tom (15)"


# test count_upper_lower_case_characters():
text = "The quick brown fox called Ferox jumps over the lazy dog's back 123 times."
count_upper_lower_case_characters(text) # should count 2 uppercase and 54 lowercase characters

# test print_even():
numbers = [0,1,2,3,4,5,6,7,8,9,10]
print_even(numbers) # should print 0, 2, 4, 6, 8, 10
```

Run the ex4_main.py file to test then functions:
```sh
python3 ex4_main.py
```

</details>

******

<details>
<summary>Exercise 5: Python Program 'Calculator'</summary>
<br />

**Tasks:**

Write a simple calculator program that:
- takes user input of 2 numbers and operation to execute
- handles following operations: plus, minus, multiply, divide
- does proper user validation and give feedback: only numbers allowed
- Keeps the Calculator program running until the user types “exit”
- Keeps track of how many calculations the user has taken, and when the user exits the calculator program, prints out the number of calculations the user did

Concepts covered: working with different data types, conditionals, type conversion, user input, user input validation

**Solution:**

```python
def validate(user_input):
    args = user_input.split()
    if (len(args) != 3):
        return { "is_valid": False, "result": "invalid number of input elements" }
    
    a1 = args[0]; a2 = args[1]; op = args[2]
    n1 = 0; n2 = 0
    
    try:
        n1 = float(a1)
        if n1.is_integer():
            n1 = int(n1)
    except ValueError:
        return { "is_valid": False, "result": "the first element is not a valid number" }
    
    try:
        n2 = float(a2)
        if n2.is_integer():
            n2 = int(n2)
    except ValueError:
        return { "is_valid": False, "result": "the second element is not a valid number" }
    
    if op != 'plus' and op != 'minus' and op != 'multiply' and op != 'divide':
        return { "is_valid": False, "result": "the third element is not a valid operation name" }

    if op == 'divide' and n2 == 0:
        return { "is_valid": False, "result": "Division by zero is not defined." }

    return { "is_valid": True, "result": [n1, n2, op] }

def int_or_float(number):
    if float(number).is_integer():
        return int(number)
    return number

def calculate(n1, n2, op):
    if op == 'plus':
        print(f"{n1} + {n2} = {int_or_float(n1 + n2)}")
    elif op == 'minus':
        print(f"{n1} - {n2} = {int_or_float(n1 - n2)}")
    elif op == 'multiply':
        print(f"{n1} * {n2} = {int_or_float(n1 * n2)}")
    elif op == 'divide':
        print(f"{n1} / {n2} = {int_or_float(n1 / n2)}")

count = 0
while True:
    user_input = input("Enter two numbers and an operation ('plus', 'minus', 'multiply', 'divide'): ")
    if (user_input == 'exit'):
        print(f"You did {count} calculation(s).")
        break
    
    validation_result = validate(user_input)
    if validation_result.get('is_valid'):
        n1 = validation_result.get('result')[0]
        n2 = validation_result.get('result')[1]
        op = validation_result.get('result')[2]
        calculate(n1, n2, op)
        count += 1
    else:
        print(validation_result.get('result'))
```

</details>

******

<details>
<summary>Exercise 6: Python Program 'Guessing Game'</summary>
<br />

**Tasks:**

Write a program that:
- runs until the user guesses a number (hint: while loop)
- generates a random number between 1 and 9 (including 1 and 9)
- asks the user to guess the number
- then prints a message to the user, whether they guessed too low, too high
- if the user guesses the number right, print out YOU WON! and exit the program

Hint: Use the built-in random module to generate random numbers https://docs.python.org/3.3/library/random.html

Concepts covered: Built-In Module, User Input, Comparison Operator, While loop

**Solution:**

```python
from random import randint

secret_number = randint(1, 9)
guess = input("Guess a number greater of equal to 1 and lower or equal to 9: ")
count = 1
found = False
while not found:
    if not guess.isnumeric():
        guess = input("The value you entered is not a number. Try again: ")
    else:
        guess_n = int(guess)
        if guess_n == secret_number:
            print(f"You won in {count} attempts!")
            found = True
        elif guess_n < secret_number:
            guess = input("Your number is to low. Try again: ")
            count += 1
        else:
            guess = input("Your number is to high. Try again: ")
            count += 1
```

</details>

******

<details>
<summary>Exercise 7: Working with Classes and Objects</summary>
<br />

**Tasks:**

Imagine you are working in a university and need to write a program, which handles data of students, professors and lectures. To work with this data you create classes and objects:

a) Create a Student class

with properties:
- first name
- last name
- age
- lectures he/she attends

with methods:
- can print the full name
- can list the lectures, which the student attends
- can add new lectures to the lectures list (attend a new lecture)
- can remove lectures from the lectures list (leave a lecture)

b) Create a Professor class

with properties:
- first name
- last name
- age
- subjects he/she teaches

with methods:
- can print the full name
- can list the subjects they teach
- can add new subjects to the list
- can remove subjects from the list

c) Create a Lecture class

with properties:
- name
- max number of students
- duration
- list of professors giving this lecture

with methods:
- printing the name and duration of the lecture
- adding professors to the list of professors giving this lecture

d) Bonus task

As both students and professors have a first name, last name and age, you think of a cleaner solution:

**Inheritance** allows us to define a class that inherits all the methods and properties from another class.
- Create a Person class, which is the parent class of Student and Professor classes
- This Person class has the following properties: "first_name", "last_name" and "age"
- and following method: "print_name", which can print the full name
- So you don't need these properties and method in the other two classes. You can easily inherit these.
- Change Student and Professor classes to inherit "first_name", "last_name", "age" properties and "print_name" method from the Person class

**Solution:**

Write the following four classes:

_ex7\_person.py_
```python
class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_name(self):
        print(f"{self.first_name} {self.last_name}")
```

_ex7\_professor.py_
```python
from ex7_person import Person

class Professor(Person):

    def __init__(self, first_name, last_name, age, subjects=[]):
        super().__init__(first_name, last_name, age)
        self.subjects = subjects
    
    def list_subjects(self):
        for subject in self.subjects:
            print(f" - {subject}")
    
    def add_subject(self, subject):
        self.subjects.append(subject)
    
    def remove_subject(self, subject):
        self.subjects.remove(subject)
```

_ex7\_student.py_
```python
from ex7_person import Person

class Student(Person):

    def __init__(self, first_name, last_name, age, lectures=[]):
        super().__init__(first_name, last_name, age)
        self.lectures = lectures
    
    def list_lectures(self):
        for lecture in self.lectures:
            print(f" - {lecture.name}")
    
    def add_lecture(self, lecture):
        self.lectures.append(lecture)
    
    def remove_lecture(self, name_of_lecture_to_remove):
        lecture_to_be_removed = None
        for lecture in self.lectures:
            if lecture.name == name_of_lecture_to_remove:
                lecture_to_be_removed = lecture
                break
        if lecture_to_be_removed != None:
            self.lectures.remove(lecture_to_be_removed)
```

_ex7\_lecture.py_
```python
class Lecture:

    def __init__(self, name, max_students, duration, professors=[]):
        self.name = name
        self.max_students = max_students
        self.duration = duration
        self.professors = professors
    
    def print_info(self):
        print(f"{self.name} ({self.duration} minutes)")
    
    def add_professor(self, professor):
        self.professors.append(professor)
```

To test the functionality of the classes, write a main script with the following content:

_ex7\_main.py_
```python
from ex7_student import Student
from ex7_professor import Professor
from ex7_lecture import Lecture

# Professor
professor = Professor("Linda", "Gray", 42, ['Linux', 'Databases'])
professor.print_name()
professor.add_subject('Programming')
professor.remove_subject('Linux')
professor.list_subjects()

# Lecture
linux_lecture = Lecture("Basic Linux Commands", 25, 45)
linux_lecture.print_info()

python_lecture = Lecture("Programming with Python", 12, 60)
python_lecture.add_professor(professor)

database_lecture = Lecture("MySQL Database Administration", 15, 90)
database_lecture.add_professor(professor)

kubernetes_lecture = Lecture("Kubernetes for Beginners", 10, 60)

# Student
student = Student("Peter", "Smith", 24, [linux_lecture, python_lecture, database_lecture])
student.print_name()
student.add_lecture(kubernetes_lecture)
student.remove_lecture("MySQL Database Administration")
student.list_lectures()
```

</details>

******

<details>
<summary>Exercise 8: Working with Dates</summary>
<br />

**Tasks:**

Write a program that:
- accepts user's birthdate as input
- calculates how many days, hours and minutes are remaining till the next birthday
- prints out the result as a message to the user

**Solution:**

```python
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
```

</details>

******

<details>
<summary>Exercise 9: Working with Spreadsheets</summary>
<br />

**Tasks:**

Write a program that:
- reads the provided spreadsheet file "employees.xlsx" (see Download section at the bottom) with the following information/columns: "name", "years of experience", "job title", "date of birth"
- creates a new spreadsheet file "employees_sorted.xlsx" with following info/columns: "name", "years of experience", where the years of experience is sorted in descending order: so the employee name with the most experience in years is on top.

**Solution:**

</details>

******

<details>
<summary>Exercise 10: Working with REST APIs</summary>
<br />

**Tasks:**

Write a program that:
- connects to GitHub API
- gets all the public repositories for a specific GitHub user
- prints the name & URL of every project

**Solution:**

</details>

******
