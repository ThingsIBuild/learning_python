# day 1  : of learning python
# # use to defined the single line comment
# ''' ''' , """ """,  use to defined the multi-line comment


# to print something on the terminal we print function

print("hello world")
print("welcome to day 1 of learning python")


# variables and data types in python

print("\n", 50 * "-", "\n")

x = 3  # number
y = 4.5  # float
name = "John"  # string
is_student = True  # boolean

check = x > y  # boolean expression

# we can type() to print the type of a variable
print(type(x), x)
print(type(y), y)
print(type(name), name)
print(type(is_student), is_student)
print(type(check), check)

print("\n", 50 * "-", "\n")
# arithmetic operations

num_1 = 3
num_2 = 10

addition = num_1 + num_2
difference = num_1 - num_2
product = num_1 * num_2
quotient = num_1 / num_2

print("Addition:", addition)
print("Subtraction:", difference)
print("Multiplication:", product)
print("Division:", quotient)

print("Modulus:", num_2 % num_1)  # remainder
print("Exponentiation:", num_1**2)  # power
print("Floor Division:", num_2 // num_1)  # quotient without decimal


# string formatting and basic I/O
print("\n", 50 * "-", "\n")
print("Hello, my name is", name)
print("I am", x, "years old.")
print("Is student:", is_student)


fav_color = input("Enter your favorite color: ")

print("Your favorite color is", fav_color)


print("\n", 50 * "-", "\n")


# function
def print_user_info(name, age, is_student):
    print("Hello, my name is", name)
    print("I am", age, "years old.")
    print("Is student:", is_student)


print_user_info("Alice", 22, True)


def product_details(product_name, price, in_stock):
    return {"name": product_name, "price": price, "in_stock": in_stock}


print(product_details("Laptop", 999.99, True))

# loops in python
print("\n", 50 * "-", "\n")
arr = [1, 2, 3, 4, 5]

for item in arr:
    print("Item:", item)


list_of_products = [
    {"name": "Laptop", "price": 999.99, "in_stock": True},
    {"name": "Mouse", "price": 49.99, "in_stock": True},
    {"name": "Keyboard", "price": 89.99, "in_stock": False},
]


for product in list_of_products:
    print(product_details(product["name"], product["price"], product["in_stock"]))

print("\n", 50 * "-", "\n")

users = [
    {"name": "arjun", "role": "developer", "category": 10},
    {"name": "vishal", "role": "designer", "category": 13},
    {"name": "priya", "role": "hr", "category": 12},
]


print("\n", 50 * "-", "\n")

for user in users:
    if user["role"] == "developer":
        print("Developer:", user["name"])
    elif user["role"] == "designer":
        print("Designer:", user["name"])
    elif user["role"] == "hr":
        print("HR:", user["name"])


print("\n", 50 * "-", "\n")


user_form_list = ["username", "email", "password"]


if len(user_form_list) < 3:
    print("Form is incomplete")
else:
    print("Form is complete")
