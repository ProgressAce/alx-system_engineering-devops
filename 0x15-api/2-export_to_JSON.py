#!/usr/bin/python3
"""This script exports the data of all the user's tasks to  json formatted file

Uses the JSOPlaceholder REST API to retrieve fake data to be act as
the employees with their TODO lists.
The chosen employee will be determined by a passed integer parameter.

The json file content format will be:
    { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}, {"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    # validating passed argument
    if len(argv) != 2:  # passed arguments start at index 1
        print('USAGE: ./<program_name> employee_id_as_integer')
        exit()
    if int(argv[1]) < 0 or int(argv[1]) > 200:
        print('employee_id should be between 0 and 200')
        exit()

    user_id = int(argv[1])
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(user_id)).json()
    # retrieve specific employee's todo list
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(user_id)).json()

    # Writing data to a JSON file

    with open('{}.json'.format(user_id), 'w') as json_file:
        json_dict = {}

        for task in todo:  # to capture all tasks
            details = {
                    'task': task['title'],
                    'completed': task['completed'],
                    'username': employee['username']
                    }
            json_dict[f'{employee['id']}'] = [details]

        json_str = json.dumps(json_dict)
        json_file.write()
