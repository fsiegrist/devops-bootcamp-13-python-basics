employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

# Update the job to 'Software Engineer'
employee['job'] = 'Software Engineer'

# Remove the age key from the dictionary
employee.pop('age')

# Loop through the dictionary and print the key:value pairs one by one
for key, value in employee.items():
    print(f"{key}:{value}")


dict_one = {'a': 100, 'b': 400} 
dict_two = {'x': 300, 'y': 200}

# Merge these two Python dictionaries into 1 new dictionary
dict_merged = dict_one.copy()
dict_merged.update(dict_two)

# Sum up all the values in the new dictionary and print it out
sum = 0
for value in dict_merged.values():
    sum = sum + value
print(f"Sum of values = {sum}")

# Print the max and minimum values of the dictionary
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
