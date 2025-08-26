
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def product_info(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def total_value(self):
        return self.price * self.quantity

    def apply_discount(self, percentage):
        discount_amount = (percentage / 100) * self.price
        self.price -= discount_amount
        return f"New price after {percentage}% discount is: {self.price}"

product1 = Product("Laptop", 1000, 5)

print(product1.product_info())
print(product1.total_value())
print(product1.apply_discount(10))
