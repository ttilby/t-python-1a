# Python - Assignment 1

## Synopsis
Accept user input to determine age on different planets

## Extra Ideas
1. Accept user input to determine age in hours, minutes, and / or seconds if birth time is entered
2. Instead of reading from the console, set up the program to parse the birthday information from a specified file

## Objectives
Entry level python
	Environment Setup using PyCharm Community
Git principles
	Forking a project
	Basic Git commands
	Peer Review
	Pull Requests
Exposure to TDD
Exposure to Makefile
Documentation

## Getting Started
1. Environment Setup - https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html
    1. Install PyCharm Community Edition
    2. Follow the instructions here to get PyCharm setup and configured. Read through "Step 1. Creating and Running Your First Python Project" get used to project set up
1. Git setup
    1. create a github.com account if you dont have one
    2. Fork this git repo: https://github.com/ttilby/t-python-1a.git`    
    3. In your new repository, find the correct https url for your git repo
2. Clone git repo
    1. open command prompt
    2. cd to folder that will hold your programming projects
    3. `git clone <your project url>` 
2. Python setup
    These steps will install the requirements for the project to ensure you
have what you need to get started.
    1. install python 3.7
    2. in command prompt, run `py -m pip --version` to ensure pip is installed
    2. inside the project folder, run `pip install -r pip-requirements.txt`
2. Open Pycharm and select open project, choose the root folder for the project
   you cloned from git.
3. Run provided unit Tests
    1. Pycharm needs to know where to search for source code
        1. Preferences --> Project: Python-1a --> Project Structure
        2. Hihglight the src folder
        3. Click "Mark as: Sources"
    2. Set up Test configuration
        1. top right of screen - click "Edit Configurations..."
        2. top left, click + --> Python tests --> pytest
        3. Fill in the following fields
            1. Name: <whatever you want>
            2. Target: Script path
            3. tests/test_planet.py
            4. Python interpreter: path for installed venv (e.g. python-1a/venv/vin/python)
            5. Working directory: Should point to the root folder of the project.
            6. OK
        4. Running the play button will show 9 failing unit tests. If you see something different, try googling the error message or ask for help.
4. Set up run configuration
    1. top right of screen - click "Edit Configurations..."
    2. top left, click on + --> Python
    3. Fill in the following fields
        1. Name: <whatever you want>
        2. Script Path: <project path>/src/space_travel.py
        3. Environment variables (default): PYTHONUNBUFFERED=1
        4. Python interpreter: <project path>/venv/bin/python
        5. Working directory: <project path>
        6. OK
    4. Clicking the Play button will allow you to run the program inside pycharm. Clicking in the console below will allow you to enter user input.

## Goal - Determine a users age on each of the nine planets
    1. use the information here to determine the revolution period of each planet:[Your age on other worlds](https://www.exploratorium.edu/ronh/age/)
    2. Collect user input to determine the user's birthday
    3. Calculate the user's age (years and days) on each of the nine planets and display the age with each planet
    4. code until all 9 unit tests pass

