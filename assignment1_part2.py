class Book():
    def __init__(self, title, author):
        self.author = author
        self.title = title

    def display(self):
        print(self.title + ", written by " + self.author)

ob1 = Book("Harry Potter and the Goblet of Fire", "J.K. Rowling")
ob1.display()

ob2 = Book("Ivanhoe: A Romance", "Walter Scott")
ob2.display()