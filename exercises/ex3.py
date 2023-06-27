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

# Print out the name, job and city of each employee using a loop
for employee in employees:
    print(f"Name: {employee.get('name')}")
    print(f"Job:  {employee.get('job')}")
    print(f"City: {employee.get('address').get('city')}")
    print("--------")

# Print the country of the second employee in the list by accessing it directly
print(f"2nd employee's country: {employees[1].get('address').get('country')}")
