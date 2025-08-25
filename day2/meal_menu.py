

# meal menu 

food_items_order = int(input("Enter the number of food item you want add: "))

food_items = []

for i in range(food_items_order):
    item = input("Enter food item name: ")
    food_items.append(item)
    print(f"{item} added to your menu.")

print(" \n Your food menu:")
for item in food_items:
    print("-", item)