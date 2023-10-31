#import requests, sys and json
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    #define base url for API
    todo_url = "https://jsonplaceholder.typicode.com"

    #get employee details
    employee_response = requests.get(f"{todo_url}/user/{employee_id}")
    employee_data = employee_response.json()
    user_id = employee_data["id"]
    username = employee_data["username"]

    #get employee todo list
    todo_response = requests.get(f"{todo_url}/users/{employee_id}/todos")
    todo_data = todo_response.json()

    #create a json file for the employee
    data = {"username": []}
    for todo in todo_data:
      complete_tasks = "completed" if todo["completed"] else "not completed"
      task_title = todo['title']
      data['username'].append({"task": task_title, "completed": complete_tasks, "username": username})

    filename = f"{user_id}.json"
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"data exported to {filename}")
   
    if __name__ == "main":
       if len(sys.argv) != 2:
          print("usage: employ_ids.py <employee_id>")
       sys.exit(1)

employee_id = int(sys.args[1])
get_employee_todo_progress(employee_id)  
       
