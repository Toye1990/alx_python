"""import requests and json module"""
import requests, sys

def get_todo_list_progress(employee_id):
   '''
     get the todo the list progress of a given employee id.

     return a dictionary containing the employee name, the number completed task
     and the total number of tasks.
   '''
   #define url
   todo_url = "https://jsonplaceholder.typicode.com"

   #get the employee details
   employee_response = requests.get(f"{todo_url}/users/{employee_id}")
   employee_data = employee_response.json()
   employee_name = employee_data['name']

   #get employee todo list
   todos_response = requests.get(f"{todo_url}/users/{employee_id}/todos")
   todo_data = todos_response.json()

   #calculate the number of completed tasks and the total number of tasks
   total_tasks = len(todo_data)
   completed_tasks = sum(1 for todo in todo_data if todo["completed"])

#print todo list progress
   print(f"employee {employee_name} is done with ({completed_tasks}/{total_tasks})")

#print the title of completed tasks
   for todo in todo_data:
      if todo["completed"]:
         print("f\t{todo['title']}")

if __name__ == "__main__":
   if len(sys.argv) != 2:
      print("usage: employids.py <employee_id>")
      sys.exit(1)

employee_id = int(sys.args[1])
get_todo_list_progress(employee_id)


