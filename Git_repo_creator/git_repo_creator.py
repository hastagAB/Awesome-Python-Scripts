# Script Name   : git_repo_creator.py
# Author        : Harish Tiwari
# Created       : 2nd October 2020
# Last Modified	: -
# Version       : 1.0.0

# Modifications :

# Description   : This python script will create a github repo from command line.

import requests
import json

user_name = input("Enter your github user name: ") 
print(user_name)

github_token = input("Enter your github token: ") 
print(github_token)

repo_name = input("Enter your repo Name: ") 
print(repo_name)

repo_description = input("Enter your repo description: ") 
print(repo_description)

payload = {'name': repo_name, 'description': repo_description, 'auto_init': 'true'}
repo_request = requests.post('https://api.github.com/' + 'user/repos', auth=(user_name,github_token), data=json.dumps(payload))
if repo_request.status_code == 422:
    print("Github repo already exists try wih other name.")
elif repo_request.status_code == 201:
    print("Github repo has created successfully.")
elif repo_request.status_code == 401:
    print("You are unauthorized user for this action.")    
