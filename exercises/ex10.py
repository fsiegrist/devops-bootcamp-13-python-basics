import requests

response = requests.get('https://api.github.com/users/fsiegrist/repos')
public_projects = response.json()

for project in public_projects:
    print(f"Project Name: {project.get('name')}")
    print(f"Project Url: {project.get('html_url')}")
    print()
