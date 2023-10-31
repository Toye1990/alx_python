"""import requests, sys and csv module"""

import requests
import sys
import csv

def get_todo_progress(employee_id):
    #define url
    todo_url = "https://jsonplaceholder.typicode.com"

    #get employee data
    employee_response = requests.get(f"{todo_url}/users/{employee_id}")
    employee_data = employee_response.json()
    user_id = employee_data['id']
    username = employee_data["username"]

    #get employee todo list
    todo_response = requests.get(f"{todo_url}/users/{employee_id}/todos")
    todo_data = todo_response.json()

    #create a csv file for employee
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"])

        for todo in todo_data:
            completed_tasks = "completed" if todo["completed"] else "not completed"
            todo_task_title = todo['title']
            csv_writer.writerow([user_id, username, completed_tasks, todo_task_title])
    print(f"data exported to {filename}")


if __name__ == "__main__":
   if len(sys.argv) != 2:
      print("usage: employee_ids.py <employee_id>")
      sys.exit(1)

employee_id = int(sys.args[1])
get_todo_progress(employee_id)     




