from models.books import Book

book1 = Book("Catcher in the Rye", "JD Salinger", "American", True)
book2 = Book("Dune", "Frank Herbert", "Sci-fi", True)

books = [book1, book2]

def add_new_book(book):
    books.append(book)
    
def remove_book(book):
    books.remove(book)