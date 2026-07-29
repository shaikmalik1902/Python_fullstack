class Book:
    def __init__(self):
        self.title = "Python Programming"
        self.author = "ABC"
        self.available = True

    def borrow_book(self):
        if self.available:
            print("Title:", self.title)
            print("Author:", self.author)
            print("Book Borrowed Successfully")
            self.available = False
        else:
            print("Book Not Available")


book = Book()

book.borrow_book()
book.borrow_book() 