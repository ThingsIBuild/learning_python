import sqlite3

db = sqlite3.connect("todos.db")


def create_todo_table():
    with db:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                status TEXT NOT NULL
            )
            """
        )


def list_tasks():
    cursor = db.execute("SELECT * FROM todos")
    if tasks := cursor.fetchall():
        print("Current To-Do List:")
        for task in tasks:
            print(f" - {task[0]} {task[1]} [{task[2]}]")
    else:
        print("No tasks found.")


def add_task(task, status):
    with db:
        db.execute("INSERT INTO todos (task, status) VALUES (?, ?)", (task, status))


def update_task(task_id, new_status):
    with db:
        cursor = db.execute(
            "UPDATE todos SET status = ? WHERE id = ?", (new_status, task_id)
        )
    if cursor.rowcount == 0:
        print("No task found with that ID.")
    else:
        print("Task updated.")


def delete_task(task_id):
    with db:
        cursor = db.execute("DELETE FROM todos WHERE id = ?", (task_id,))
        if cursor.rowcount == 0:
            print("No task found with that ID.")
        else:
            print("Task deleted.")


def print_menu():
    print("\nWelcome to the To-Do List Manager!")
    print("1. List All Tasks")
    print("2. Add New Task")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit")
def main():
    create_todo_table()

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            list_tasks()
        elif choice == "2":
            task = input("Enter task description: ")
            status = input("Enter task status (e.g., pending, completed): ")
            add_task(task, status)
            print("Task added.")
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            new_status = input("Enter new status: ")
            update_task(task_id, new_status)
            print("Task updated.")
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
            print("Task deleted.")
        elif choice == "5":
            print("Exiting the To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
