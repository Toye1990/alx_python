import requests
import sys
import json

def export_todo_file():
#define base url for API
 todo_url = "https://jsonplaceholder.typicode.com"

 all_employee_data = {}

 #loop through all employee iDs
 for employee_id in range(1, 11):
 #get employee details
   employee_response = requests.get(f"{todo_url}/users/{employee_id}")
   if employee_response.status_code == 200:
      employee_data = employee_response.json()
      user_id = employee_data['id']
      username = employee_data['username']

      #get todo list
      todo_response = requests.get(f"{todo_url}/user/{employee_id}/todos")
      todo_data = todo_response.json()

      #create a list to store the current emmployee
      employee_tasks = []

    #populate the list with task data
      for todo in todo_data:
        complete_tasks = "completed" if todo['completed'] else "not completed"
        task_title = todo_data['title']
        employee_tasks.append({"task": task_title, "completed": complete_tasks, "username": username} )

    #store the task for current employee
      all_employee_data[user_id] = employee_tasks
    
    #create json file for all employee
      filename = "todo_all_employee.json"
      with open(filename, 'w') as json_file:
        json.dump(all_employee_data, json_file, indent=4)
      print(f"data for all employee exported to {filename}")

if __name__ == "main":
       if len(sys.argv) != 2:
          print("usage: employ_ids.py <employee_id>")
       sys.exit(1)

employee_id = int(sys.args[1])
export_todo_file(employee_id)





