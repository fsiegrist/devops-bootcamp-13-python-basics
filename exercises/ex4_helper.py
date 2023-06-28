# accepts a list of dictionaries with employee age and prints out the name and age of the youngest employee.
def print_youngest(employees):
    youngest = employees[0]
    for employee in employees:
        if int(employee.get('age')) < int(youngest.get('age')):
            youngest = employee
    print(f"{youngest.get('name')} ({youngest.get('age')})")

# accepts a string and calculates the number of upper case letters and lower case letters
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


# prints the even numbers from a provided list
def print_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)

