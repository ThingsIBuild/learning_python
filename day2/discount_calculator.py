
# discount price calculator

price = float(input("Enter the original price: "))

def apply_discount(price):
    if price > 1000:
        discount = price * 0.2
    elif price > 500:
        discount = price * 0.1
    else:
        discount = 0
    return price - discount

final_price = apply_discount(price)
print(f"The final price after discount is: {final_price}")