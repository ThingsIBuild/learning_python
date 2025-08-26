
class Books:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def is_long_book(self):
        return self.pages > 300

book1 = Books("The Great Gatsby", "F. Scott Fitzgerald", 218)

print(book1.book_info())
print(book1.is_long_book())