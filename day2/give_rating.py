

user_rating = int(input("Please enter your rating (1-5): "))

rate = ""

for i in range(user_rating):
    rate += "⭐"
print("Your rating:", rate)