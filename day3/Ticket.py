
class Ticket:
    def __init__(self, event, date, price):
        self.event = event
        self.date = date
        self.price = price

    def ticket_info(self):
        return f"Event: {self.event}, Date: {self.date}, Price: {self.price}"

    def apply_discount(self, percentage):
        discount_amount = (percentage / 100) * self.price
        self.price -= discount_amount
        return f"New price after {percentage}% discount is: {self.price}"

ticket1 = Ticket("Concert", "2023-09-15", 100)

print(ticket1.ticket_info())
print(ticket1.apply_discount(15))
