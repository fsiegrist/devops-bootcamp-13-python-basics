## Demo Project - API Request to GitLab

### Topics of the Demo Project
API Request to GitLab

### Technologies Used
- Python
- GitLab
- PyCharm
- Git

### Project Description
Write an application that talks to an API of an external application (GitLab) and lists all the public GitLab repositories for a specified user.


#### Solution
The HTTP library we're gonna use is called `requests` (see [Requests](https://pypi.org/project/requests/)).

```sh
pip3 install requests
# ...
# Successfully installed certifi-2023.5.7 charset-normalizer-3.1.0 idna-3.4 requests-2.31.0 urllib3-2.0.3
```

Create a Python file called `main.py` with the following content:

_main.py_
```python
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
```