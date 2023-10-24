#!/usr/bin/python3
"""This script exports the data of all the employees' tasks to a
json formatted file.

Uses the JSOPlaceholder REST API to retrieve fake data to act as
the employees with their TODO lists.

Records all tasks from all employees.
The json file content format will be:
    { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}, {"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
"""

import json
import requests
from sys import argv


if __name__ == '__main__':

    # request all 10 users' data from the api
    employees = requests.get('https://jsonplaceholder.typicode.com/users'
                             ).json()

    # Writing data to a JSON file

    with open('todo_all_employees.json', 'w') as json_file:

        todos_dict = {}  # todo dictionary for all users/employees.

        # employees = [{id: , name: ...}, {id: , name: ...}, ...]
        for user in employees:
            # request the specific user's todo data from the api
            todo = requests.get('https://jsonplaceholder.typicode.com/todos?' +
                                'userId={}'.format(user['id'])).json()

            # todo = [{userId: , id: , title: ...}, {userId: , id: ...}, ...]

            list_placeholder = []

            for task in todo:  # to capture all tasks
                task_dict = {
                        'username': user['username'],
                        'task': task['title'],
                        'completed': task['completed']
                        }
                list_placeholder.append(task_dict)

            todos_dict[user["id"]] = list_placeholder

        # todos_dict = a dict of users with each user having a list of tasks
        # with each task detailed in a dict
        # todos_dict = {User_Id: [{details of task1}, {details of task2}, ...],
        #               User_Id: [{details of task1}, ...]}
        json_str = json.dumps(todos_dict)
        json_file.write(json_str)
