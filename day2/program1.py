
print("Program 1: Task List Manager")

tasks = []

number_of_tasks = int(input("Enter the number of tasks you want to add: "))

for i in range(number_of_tasks):
    task = input(f"Enter task {i + 1}: ")
    tasks.append(task)
    print(f"Task {i + 1} added.")
    
print("\nYour Tasks:")
for idx, task in enumerate(tasks, start=1):
    print(f"{idx}. {task}")
    
    

print("Program 2: Salary Estimator with bonus")

