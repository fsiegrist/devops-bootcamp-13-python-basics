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
