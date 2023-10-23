#!/usr/bin/python3
"""Returns the information of an employee's TODO list progress.

Uses the JSOPlaceholder REST API to retrieve fake data to be act as
the employees with their TODO lists.
The chosen employee will be determined by a passed integer parameter."""

import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) != 2:  # passed arguments start at index 1
        print('USAGE: ./<program_name> employee_id_as_integer')
        exit()

    if int(argv[1]) < 0 or int(argv[1]) > 200:
        print('employee_id should be between 0 and 200')
        exit()

    employee_id = int(argv[1])
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(employee_id)).json()
    # retrieve specific employee's todo list
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(employee_id)).json()

    num_of_tasks = 0
    num_of_finished_tasks = 0

    for task in todo:
        if task['completed'] is True:
            num_of_finished_tasks += 1

        num_of_tasks += 1

    print('Employee {} is done with tasks({}/{}):'.
          format(employee['name'], num_of_finished_tasks, num_of_tasks))
    for task in todo:
        if task['completed'] is True:
            print('\t {}'.format(task['title']))
