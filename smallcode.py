class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

book = Book("Noli Me Tangere", "Jose Rizal")
book.display_info()