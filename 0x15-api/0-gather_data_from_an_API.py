import requests
import sys


def get_user(user_id):
    try:
        user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
        user_response.raise_for_status()
        user_data = user_response.json()
        
        todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos', params={'userId': user_id})
        todos_response.raise_for_status()
        todos_data = todos_response.json()
        
        return user_data, todos_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


def show_progress(user, todos):
    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)
    num_completed_tasks = len(completed_tasks)
    
    print(f"Employee {user['name']} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <user_id>")
        sys.exit(1)
    
    user_id = sys.argv[1]
    user, todos = get_user(user_id)
    show_progress(user, todos)
