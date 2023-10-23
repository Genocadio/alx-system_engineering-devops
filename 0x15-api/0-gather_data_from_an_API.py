#!/usr/bin/python3
"""Returns information about his/her TODO list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos?userId={}".format(user_id)).json()

    completed = [t for t in todo if t.get("completed")]
    num_completed_tasks = len(completed)
    total_tasks = len(todo)

    # Create a file to store the output
    with open("student_output", "w") as output_file:
        output_file.write("Employee {} is done with tasks({}/{}):\n".format(
            user.get("name"), num_completed_tasks, total_tasks))
        for task in completed:
            output_file.write("\t{}\n".format(task.get("title")))
