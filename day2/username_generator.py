import random , math

# user name generator

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

username = first_name.lower() + "_" + str(math.floor(random.random() * 10000)) 
print("Your generated username is:", username)
