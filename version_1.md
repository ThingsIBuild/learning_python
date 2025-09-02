# Python, Gently: A Practical Guide for Programmers Coming from Other Languages And Self Learners

## Introduction

Welcome! This article series teaches Python from the ground up without assuming you’re a total beginner to programming. If you’ve written code in languages like C/C++, Java, JavaScript/TypeScript, Go, or Ruby, you’ll find side‑by‑side explanations that map familiar concepts to Python’s syntax and idioms.

By the end, you’ll be able to read and write clean Python, and you’ll ship a small but useful Sales Generator CLI that stores data in SQLite.

## Who this is for

- Developers comfortable with basic programming concepts (variables, loops, functions) who are new to Python.

- Self‑learners who like lots of tiny exercises and a hands‑on project.


## What you’ll learn

- Python’s core syntax and how it differs from other languages (indentation over braces, dynamic typing, truthiness, slicing, etc.).

- Practical use of lists, tuples, (and when we get to JSON, we’ll introduce dictionaries), plus control flow and functions.

- How to design and build a command‑line app with argument parsing, data validation, persistence with SQLite, and simple reporting.


## How this guide is organized

### 1. Section 1 — Learning the SyntaxWe’ll tackle one topic at a time:

- Comments
- Variables
- Data types
- Conditional statements
- Loops
- Functions, scope, and return values
- Tuples and Lists (and when working with JSON, we’ll naturally meet Dictionaries)
- JSON basics

After each topic you’ll get 2–4 quick exercises before moving on.

### Section 2 — Project: Sales Generator CLI (SQLite)We’ll apply the syntax you learned to build a small app with features to:

- Add a sale
- View sales
- Update a sale
- Delete a sale
- Generate a sales report
- Exit the app cleanly


### What you need

- Python 3.x installed (any recent 3.x is fine).
- A terminal (macOS/Linux shell, or Windows Terminal/PowerShell).
- A text editor (VS Code, Zed, Sublime, etc.).
- SQLite comes bundled with Python via the sqlite3 module, so no extra database server is required.


## How you’ll run code in this guide

You can use either the REPL or script files.
#### Check Python is available
```py
python3 --version   # or: python --version
```


### Use the REPL for quick experiments
```py
python3
>>> print("Hello, Python!")
Hello, Python!
>>> exit()
```

#### Run a script file

```bash
echo 'print("Hello from a script")' > hello.py
python3 hello.py
```

### Conventions we’ll use

- Code blocks are in Python 3.
- #comments show notes inside code.
- We’ll prefer clear, beginner‑friendly examples over clever tricks.


## Quick Setup Exercise (before we start)

- Do these now so you’re ready for the first syntax topic:
- Verify your Python version prints something like Python 3.10.x or higher.
- Open the REPL and print your name: print("Hi, I am <your name>").
- Create a playground.py file with a single line print("Ready to learn!") and run it.
- If that all worked, you’re set. In the next section, we’ll start with “What is Python?” to put the language in context before diving into comments and variables.



# What is Python?

Python is a high‑level, interpreted programming language known for its readability and simplicity. Its design philosophy emphasizes clarity and reducing “boilerplate” code — which is why it’s often described as executable pseudocode.

A few quick points to understand:

- Created in 1991 by Guido van Rossum and now maintained by the Python Software Foundation.
- Widely used in web development, data analysis, AI/ML, scripting, and automation.
- Popular for its large ecosystem of libraries (NumPy, Pandas, Django, Flask, FastAPI, etc.).


Why programmers love Python

- Readable syntax: You don’t need curly braces {} or semicolons ;. Indentation defines code blocks.
- Dynamic typing: No need to declare types explicitly. Variables can hold different types over their lifetime.
- Cross‑platform: Runs everywhere — Windows, Linux, macOS.
- Massive community: You’ll always find tutorials, forums, and libraries.

## Compare at a glance

Here’s a tiny side‑by‑side snippet of a “Hello, World” in Java vs. Python:

#### Java
```java
class HelloWorld {
public static void main(String[] args) {
System.out.println("Hello, World");
}
}
```
#### Python
```py
print("Hello, World")
```
That’s the essence: Python tries to remove ceremony and get straight to the logic.

## Comments in Python

Comments are notes you leave in your code for yourself or other programmers. They’re ignored by Python when the program runs.

### Single-line comments

Use the # symbol. Everything after it on that line is ignored.

```markdown
# This is a comment
print("Hello") # This comment explains the line
```

### Multi-line comments (docstrings)

Python doesn’t have true multi-line comments like /* ... */ in C/Java, but you can use triple quotes (''' or """) as block comments or documentation strings:

```markdown
"""
This is a multi-line comment or docstring.
It can describe what a function or file does.
"""
print("Python comments demo")
```
Docstrings are often used for documenting functions, classes, or modules.


Why comments matter

- They explain why you wrote code a certain way.
- They make collaboration easier.
- They serve as reminders for future you!

### Exercises — Comments

- Write a program that prints your favorite color. Add a single-line comment explaining the choice.
- Add a multi-line docstring at the top of your program describing what the program does.
- Try writing code without comments, then go back and add comments to explain tricky parts. Notice the difference.


## Variables in Python

A variable is simply a name that refers to a value in memory. Unlike C, Java, or Go, you don’t declare a type when creating a variable in Python — it’s dynamically assigned.

#### Declaring variables

```py
name = "Vishal" # string
age = 25 # integer
height = 5.9 # float
is_student = True # boolean
```

Key differences vs. other languages

- No need for type keywords like int, string, or boolean.
- Assignment uses a single equals sign =.
- Variable names follow snake_case convention (e.g., total_sales).
- Case-sensitive: Name and name are different variables.


## Reassigning variables

You can change the type of value stored:

```py
x = 10
x = "Now I’m a string"
print(x) # Output: Now I’m a string
```
This flexibility is powerful but requires careful handling in larger programs.

## Multiple assignments

Python allows assigning multiple variables in one line:

```py
a, b, c = 1, 2, 3
print(a, b, c) # Output: 1 2 3
```

Or giving the same value to multiple variables:

```py

x = y = z = 0
print(x, y, z) # Output: 0 0 0
```

Exercises — Variables

- Define a variable name and assign your own name to it.
- Create three variables: city, country, and population. Assign appropriate values.
- Reassign a variable from an integer to a string. Print it before and after.
- Swap the values of two variables a and b in one line using Python’s multiple assignment.


# Data Types in Python

Python provides several built-in data types. Understanding them is key to writing effective code.

Numbers

- Integers (int): Whole numbers.
- Floats (float): Numbers with decimals.
- Complex numbers (complex): Rare in everyday code.

```py
x = 10       # int
y = 3.14     # float
z = 2 + 3j   # complex
```

## Strings

A string is text inside quotes.
```py
message = "Hello, World!"
print(message.upper())  # HELLO, WORLD!
```

Python strings are powerful — they support slicing:

```py
word = "Python"
print(word[0:3])  # Pyt
print(word[-1])   # n
```

## Booleans

Boolean values are either True or False.

```py
is_active = True
print(5 > 3)  # True
```

## Lists

Lists are ordered, mutable collections.
```py
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']
```

## Tuples

Tuples are like lists but immutable (cannot be changed).

```py
coordinates = (10, 20)
print(coordinates[0])  # 10
```

## Dictionaries

Dictionaries store data as key-value pairs.

```py
person = {"name": "Alice", "age": 30}
print(person["name"])  # Alice
```


## Type checking

Use type() to inspect a variable’s type.

```py
x = 42
print(type(x))  # <class 'int'>
```

## Exercises — Data Types

- Create a variable temperature with a float value. Print its type.
- Define a string greeting and print the first 3 characters.
- Make a list of 5 countries. Add one more country to it.
- Define a tuple with your birth year and birth month.
- Create a dictionary with keys title and author for your favorite book.


## Conditional Statements in Python

Conditionals let you execute different code based on whether a condition is true or false.

#### If statement

```py
x = 10
if x > 5:
    print("x is greater than 5")
```
Notice: indentation matters in Python. No {} braces — the block is defined by spaces.

#### If-else
```py
    age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

#### Elif (else if)

```py
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")

```

### Comparison operators

*   `==` equal
*   `!=` not equal
*   `<`, `>`, `<=`, `>=`
    

### Logical operators

*   `and` (both true)    
*   `or` (at least one true)
*   `not` (negation)


```py
x = 10
y = 20
if x > 5 and y > 15:
    print("Both conditions are true")
```

### Exercises

1.  Write a program that checks if a number is positive, negative, or zero.
2.  Create a variable `age` and print whether the person is a child (<13), teenager (13–19), or adult (20+).
3.  Write a program that checks if a number is divisible by both 2 and 3.


## Loops in Python

Loops let you repeat code multiple times.

### For Loop

Iterates over a sequence (list, tuple, string, range).

```py
# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop over a range of numbers
for i in range(5):  # 0 to 4
    print(i)
```


### While Loop

Repeats as long as a condition is true.


```py
count = 0
while count < 5:
    print(count)
    count += 1
```

### Break and Continue

- break exits the loop immediately.
- continue skips the rest of the loop and goes to the next iteration.


```py
for i in range(5):
    if i == 3:
        break  # exits loop
    print(i)

for i in range(5):
    if i == 3:
        continue  # skips 3
    print(i)
```

for i in range(5):
    if i == 3:
        break  # exits loop
    print(i)

for i in range(5):
    if i == 3:
        continue  # skips 3
    print(i)
Exercises

    1. Print numbers from 1 to 10 using a for loop.
    2. Print all even numbers from 0 to 20 using a while loop.
    3. Iterate over a list of 5 names and print each name.
    4. Use a loop to find the first number divisible by 7 between 1 and 50 and break when found.


## Functions, Scope, and Return Values

Functions let you group code into reusable blocks. Python functions are defined with def.

### Defining a function
```py
def greet(name):
    print(f"Hello, {name}!")
```

### Calling a function
```py
greet("Vishal")  # Hello, Vishal!
```

### Function arguments and return values

```py
def add(a, b):
    return a + b

result = add(5, 7)
print(result)  # 12
```

### Default arguments

```py
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()       # Hello, Guest!
greet("Alice") # Hello, Alice!
```

## Scope

- Local variables: defined inside a function, only accessible there.
- Global variables: defined outside functions, accessible anywhere.

```py
x = 10  # global

def my_func():
    y = 5  # local
    print(x, y)

my_func()  # 10 5
# print(y)  # Error: y is not defined
```


## Exercises

1. Write a function square that returns the square of a number.
2. Create a function is_even that returns True if a number is even, False otherwise.
3. Write a function that takes a name and prints a greeting, with a default value for the name.
4. Experiment with a local variable inside a function and try accessing it outside (observe the error).


## Tuples, Lists, and JSON Basics



###  Tuples

Tuples are ordered, immutable collections. Once you create a tuple, you cannot change its values.

```py
point = (10, 20)
print(point[0])  # 10
print(point[1])  # 20
```

- Useful for fixed collections of items.
- Can be used as keys in dictionaries because they are immutable.

### Lists

Lists are ordered, mutable collections. You can add, remove, or change items.

```py
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry', 'orange']
```

- Lists support slicing, iteration, and various built-in methods like append(), pop(), remove().

### JSON
```py
import json

# Python dict to JSON string
data = {"name": "Vishal", "age": 25}
json_str = json.dumps(data)
print(json_str)  # '{"name": "Vishal", "age": 25}'

# JSON string to Python dict
parsed = json.loads(json_str)
print(parsed['name'])  # Vishal

```

- JSON is great for saving structured data or exchanging it with APIs.
- Python's json module handles serialization and deserialization easily.


### Exercises

- Create a tuple coordinates with values 10 and 20, and print both values.
- Create a list colors with 3 color names, add another color using append, and then change the first color.
- Convert a Python dictionary {"product": "book", "price": 200} into a JSON string and print it.
- Parse the JSON string back into a dictionary and print the value of product.
- Experiment by creating a list of dictionaries representing 3 students with keys name and score.