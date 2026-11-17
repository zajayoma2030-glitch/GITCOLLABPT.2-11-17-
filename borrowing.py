from library import Book

class BorrowBook(Book):
    def borrow(self):
        print(self.title, "is borrowed.")

book =BorrowBook("Noli Me Tangere")
book.display()
book.borrow()