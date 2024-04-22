import requests
import sys


def fetch_todo_list(employee_id):
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        employee_id)
    response = requests.get(url)
    todos = response.json()
    return todos


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    todos = fetch_todo_list(employee_id)

    # Extract employee name
    employee_name = todos[0]['name']

    # Count completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)

    # Total number of tasks
    total_tasks = len(todos)

    # Print employee's progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t", task['title'])


if __name__ == "__main__":
    main()

