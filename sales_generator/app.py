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
