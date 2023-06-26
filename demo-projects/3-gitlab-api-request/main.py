import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
projects = response.json()

# print the whole objects list
print(projects)
print(type(projects))     # list
print(type(projects[0]))  # dict

# print just the names and urls
for project in projects:
    print(f"Project Name: {project.get('name')}\nProject URL: {project.get('http_url_to_repo')}\n")
