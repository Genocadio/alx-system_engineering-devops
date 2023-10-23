#!/usr/bin/python3
"""export data in the JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({user.get("id"): [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        } for task in todos if task.get("userId") == user.get("id")]
            for user in users}, jsonfile)
