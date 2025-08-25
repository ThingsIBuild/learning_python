base_salary = float(input("Enter your base salary: "))
year_of_experience = int(input("Enter your years of experience: "))


if year_of_experience > 3:
    bonus = base_salary * 0.2
    total_salary = base_salary + bonus
    print(f"Your total salary including bonus is: {total_salary}")
    
else:
     print("you are not eligible for a bonus.")
     print(f"Your total salary is: {base_salary}")

