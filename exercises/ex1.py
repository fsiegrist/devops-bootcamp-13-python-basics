my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]

# Print elements >= 10
for number in my_list:
    if number >= 10:
        print(number)

# Make a new list with all elements higher than or equal 10 and print it out
new_list = []
for number in my_list:
    if number >= 10:
        new_list.append(number)
print(new_list)

# User input as a number and print a list that contains only those elements from my_list that are higher than the number given by the user.
threshold = input("Enter a number: ")
new_list = []
for number in my_list:
    if number > int(threshold):
        new_list.append(number)
print(new_list)
