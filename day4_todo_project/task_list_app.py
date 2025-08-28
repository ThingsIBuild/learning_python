import json

with open("tasks.json", "r") as file:
    tasks = json.load(file)


def list_tasks(tasks):
    for task in tasks:
        print(f"{task['id']}. {task['title']} - {'✓' if task['completed'] else '✗'}")


def add_task(title, is_completed=False):
    new_id = max(task["id"] for task in tasks) + 1
    tasks.append({"id": new_id, "title": title, "completed": is_completed})
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
        
        


def mark_task_complete(task_id, is_completed):
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = is_completed
            break
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
        print('task updated successfully')



def delete_task(task_id):
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    tasks = [task for task in tasks if task["id"] != task_id]
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
        print('task deleted successfully')


def main():
    print("Welcome to the Task List App!")
    print("1. To list all the tasks")
    print("2. To add a new task")
    print("3. To mark a task as complete")
    print("4. To delete a task")
    print("\n ", 50 * "-", "\n")
    user_input = input("Enter your choice: ")
    if user_input == "1":
        list_tasks(tasks)
    elif user_input == "2":
        title = input("Enter task title: ")
        is_completed = (
            input("Is the task completed? (yes/no): ").strip().lower() == "yes"
        )
        add_task(title, is_completed)

        list_tasks(tasks)
    elif user_input == "3":
        task_id = int(input("Enter task ID to mark as complete: "))
        change_status = (
            input("Is the task completed? (yes/no): ").strip().lower() == "yes"
        )
        mark_task_complete(task_id, change_status)
    elif user_input == "4":
        task_id = int(input("Enter task ID to delete: "))
        delete_task(task_id)
        list_tasks(tasks)
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
