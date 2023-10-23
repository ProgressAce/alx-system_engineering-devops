#!/usr/bin/python3
"""This script exports the data of all the user's tasks to a csv formatted file

Uses the JSOPlaceholder REST API to retrieve fake data to be act as
the employees with their TODO lists.
The chosen employee will be determined by a passed integer parameter.

The csv file content format will be:
    'USER_ID','USERNAME','TASK_COMPLETED_STATUS','TASK_TITLE'"""

from sys import argv
import requests
import csv


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

    # Writing data to a CSV file

    with open('{}.csv'.format(user_id), 'w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todo:  # to capture all tasks
            line = [
                    employee['id'],
                    employee['username'],
                    task['completed'],
                    task['title']
                    ]

            csv_writer.writerow(line)
