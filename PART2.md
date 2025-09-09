# Section 2: Building a Sales Generator CLI Application with SQLite

## Introduction

In the first part of this article, we explored Python’s basic syntax: variables, data types, loops, conditionals, functions, and working with collections like lists, tuples, and JSON. Now, it’s time to put that knowledge into practice by building something useful.

We’ll be creating a Sales Generator CLI (Command Line Interface) Application using Python and SQLite. This project will allow us to:


1. `Add a sale ` (store details like product, quantity, and price).
2. ` View all sales` (see the list of sales we’ve added).
3. ` Update a sale` (change details if we entered something wrong).
4. ` Delete a sale` (remove unwanted sales records).
5. ` Generate` a sales report (calculate total sales).
6. ` Exit` the application when we’re done.


By the end of this section, you’ll understand how to:

    - Work with SQLite, a lightweight database that comes bundled with Python.
    - Write functions that interact with a database.
    - Use loops and conditionals to create a menu-driven CLI app.


## Why SQLite?

SQLite is a database engine that comes pre-installed with Python. Unlike larger databases like MySQL or PostgreSQL, it doesn’t require setting up a server. Instead, it stores data in a single file on your computer, making it perfect for small projects and learning.

## Project Setup

Before we dive into coding, let’s set up our project folder:
1. Create a new folder called sales_generator.
2.  Inside it, create a file named app.py. This will contain our application code.
3. We’ll also create a database file automatically when we run the app for the first time.

Your folder should look like this:

```js
sales_generator/
 └── app.py

```

## Step 1: Setting Up the Database

Before we can add or view sales, we need a place to store our data. That’s where SQLite comes in.

Python provides a built-in library called sqlite3, which we’ll use to:

1. Connect to a database file (if it doesn’t exist, it will be created).
2. Create a sales table with columns for id, product, quantity, and price.

### Code: Database Initialization

Inside your app.py file, write the following code:

```py
import sqlite3

# Function to initialize database and create table if not exists
def init_db():
    # Connect to SQLite database (creates file if it doesn’t exist)
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Save changes and close connection
    conn.commit()
    conn.close()

# Run this function once at start
if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!")

```


### Explanation

- `sqlite3.connect("sales.db")` → Connects to a database file named `sales.db`. If it doesn’t exist, Python creates it automatically.
- `cursor.execute(...)` → Executes SQL commands (in this case, creating a table).
- `CREATE TABLE IF NOT EXISTS` → Makes sure we don’t accidentally recreate the table if it already exists.
- `commit()` → Saves changes.
- `close()` → Closes the connection to avoid memory leaks.


### Try it Yourself

1. Save the file and run:

```bash
python app.py

```

2. You should see:

```bash
Database initialized successfully!
```

3. A new file sales.db will appear in your project folder. This is your SQLite database file. 🎉


## Step 2: Add a Sale

Now that we have a database with a sales table, we can start adding new sales records.
A sale will have:

- Product name (string)
- Quantity (integer)
- Price (float/decimal)

We’ll ask the user to enter these details, then store them in the database.

### Code: Add Sale Function

Add this function to your app.py (below init_db()):


```py

def add_sale():
    # Take input from user
    product = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    # Connect to database
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    # Insert data into sales table
    cursor.execute(
        "INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)",
        (product, quantity, price)
    )

    # Save changes and close
    conn.commit()
    conn.close()

    print("✅ Sale added successfully!")

```

### Why ? in SQL Query?

Instead of directly inserting variables into the SQL string, we use placeholders (?). This prevents SQL injection attacks and makes our code safer.


### Updating Main Program Flow

Now let’s add a simple menu so we can call add_sale() when the user selects the option.

Update the bottom of your file:

```py
if __name__ == "__main__":
    init_db()

    while True:
        print("\n--- Sales Generator CLI ---")
        print("1. Add a Sale")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_sale()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.")

```

### Try it Yourself

1. Run your program again:

```bash
python app.py

```

2. You should see the menu:
```bash
--- Sales Generator CLI ---
1. Add a Sale
6. Exit

```

3. If you select 1, the app will ask for product, quantity, and price, then save it to the database.

4. You can exit with 6.


## Step 3: View Sales

This feature will:

- Connect to the sales.db database.
- Fetch all records from the sales table.
- Display them in a nice format.


### Code: View Sales Function

Add this function to your app.py:

```py
def view_sales():
    # Connect to database
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    # Fetch all sales
    cursor.execute("SELECT * FROM sales")
    sales = cursor.fetchall()

    conn.close()

    if sales:
        print("\n--- Sales Records ---")
        for sale in sales:
            print(f"ID: {sale[0]} | Product: {sale[1]} | Quantity: {sale[2]} | Price: {sale[3]}")
    else:
        print("\n⚠️ No sales found.")

```
### Updating the Menu

Now update the loop at the bottom of your file to include this new option: view sales function

```py
if __name__ == "__main__":
    init_db()

    while True:
        print("\n--- Sales Generator CLI ---")
        print("1. Add a Sale")
        print("2. View Sales")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_sale()
        elif choice == "2":
            view_sales()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.")
```

### Try it Yourself

1. Run the app:
```bash
python app.py
```

2. Add a few sales (choose option 1).
3. Then select option 2 (View Sales) → You should see something like:
```yaml
--- Sales Records ---
ID: 1 | Product: Apple | Quantity: 10 | Price: 5.5
ID: 2 | Product: Banana | Quantity: 20 | Price: 2.0

```

## Step 4: Update a Sale

Sometimes, we might enter the wrong product name, quantity, or price. Instead of deleting and re-adding, we’ll allow the user to update an existing record.

The flow will be:

1. Show existing sales (so the user knows the ID).
2. Ask for the ID of the sale to update.
3. Ask for new values (product, quantity, price).
4. Update the record in the database.

### Code: Update Sale Function

Add this function to your app.py:

```py
def update_sale():
    view_sales()  # Show current sales so user can pick an ID
    
    try:
        sale_id = int(input("\nEnter the ID of the sale to update: "))
        new_product = input("Enter new product name: ")
        new_quantity = int(input("Enter new quantity: "))
        new_price = float(input("Enter new price: "))

        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE sales SET product = ?, quantity = ?, price = ? WHERE id = ?",
            (new_product, new_quantity, new_price, sale_id)
        )

        if cursor.rowcount == 0:
            print("❌ No sale found with that ID.")
        else:
            print("✅ Sale updated successfully!")

        conn.commit()
        conn.close()

    except ValueError:
        print("⚠️ Invalid input. Please enter correct values.")
```

### Updating the Menu

Add an option for Update Sale:

```py
if __name__ == "__main__":
    init_db()

    while True:
        print("\n--- Sales Generator CLI ---")
        print("1. Add a Sale")
        print("2. View Sales")
        print("3. Update a Sale")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_sale()
        elif choice == "2":
            view_sales()
        elif choice == "3":
            update_sale()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.")

```

### Try it Yourself

1. Run the program:

```bash
python app.py
```
2. Add a couple of sales (option 1).
3. View sales (option 2) and note an ID.
4. Update that sale using option 3.
5. View sales again → You should see the updated record.


## Step 5: Delete a Sale

If a sale was added by mistake, we need a way to remove it.
The flow will be:

- Show existing sales (so the user can see IDs).
- Ask for the ID of the sale to delete.
- Delete that record from the database.


### Code: Delete Sale Function

Add this function to your app.py:

```py
def delete_sale():
    view_sales()  # Show current sales so user can pick an ID

    try:
        sale_id = int(input("\nEnter the ID of the sale to delete: "))

        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM sales WHERE id = ?", (sale_id,))

        if cursor.rowcount == 0:
            print("❌ No sale found with that ID.")
        else:
            print("✅ Sale deleted successfully!")

        conn.commit()
        conn.close()

    except ValueError:
        print("⚠️ Invalid input. Please enter a valid ID.")

```

### Updating the Menu

Now add Delete a Sale as option 4:

```py
if __name__ == "__main__":
    init_db()

    while True:
        print("\n--- Sales Generator CLI ---")
        print("1. Add a Sale")
        print("2. View Sales")
        print("3. Update a Sale")
        print("4. Delete a Sale")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_sale()
        elif choice == "2":
            view_sales()
        elif choice == "3":
            update_sale()
        elif choice == "4":
            delete_sale()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.")
```

### Try it Yourself

1. Run the program.
2. Add a few sales (option 1).
3. View them (option 2) to check IDs.
4. Delete one sale using option 4.
5. View sales again → That sale should be gone.


### Step 6: Sales Report

A report will help us see:

- Total number of sales
- Total items sold (sum of all quantities)
- Total revenue (sum of quantity × price)


### Code: Sales Report Function

- Add this function to your app.py:

```py
def sales_report():
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    # Get total number of sales
    cursor.execute("SELECT COUNT(*) FROM sales")
    total_sales = cursor.fetchone()[0]

    # Get total items sold
    cursor.execute("SELECT SUM(quantity) FROM sales")
    total_items = cursor.fetchone()[0] or 0  # handle None if no sales

    # Get total revenue
    cursor.execute("SELECT SUM(quantity * price) FROM sales")
    total_revenue = cursor.fetchone()[0] or 0.0

    conn.close()

    print("\n--- Sales Report ---")
    print(f"📊 Total Sales Records: {total_sales}")
    print(f"📦 Total Items Sold: {total_items}")
    print(f"💰 Total Revenue: {total_revenue:.2f}")

```

## Updating the Menu

Add Sales Report as option 5:

```py
if __name__ == "__main__":
    init_db()

    while True:
        print("\n--- Sales Generator CLI ---")
        print("1. Add a Sale")
        print("2. View Sales")
        print("3. Update a Sale")
        print("4. Delete a Sale")
        print("5. Sales Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_sale()
        elif choice == "2":
            view_sales()
        elif choice == "3":
            update_sale()
        elif choice == "4":
            delete_sale()
        elif choice == "5":
            sales_report()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.")

```

### Try it Yourself

Run the app.

- Add a few sales (example: Apple → qty 10, price 5.5).
- Add another (Banana → qty 20, price 2.0).
- Select option 5 (Sales Report) → You should see something like:

```yaml
--- Sales Report ---
📊 Total Sales Records: 2
📦 Total Items Sold: 30
💰 Total Revenue: 95.00

```

✅ Now we have a fully functional CLI app with:

- Add Sale
- View Sales
- Update Sale
- Delete Sale
- Sales Report
- Exit