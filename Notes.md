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