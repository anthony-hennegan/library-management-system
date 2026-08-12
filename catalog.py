from utils import format_name

class Book:
    def __init__(self, title, author, checked_out=False):
        self.title = title
        self.author = author
        self.checked_out = checked_out
        
    def checkout(self):
        if self.checked_out:
            return False
        
        self.checked_out = True
        return True
    
    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            return True
        
        return False
    
class Library:
    def __init__(self, name, book_list):
        self.name = name
        self.books = book_list
    
    def find_book(self, title):
        normalized_title = title.strip().lower()
        
        for book in self.books:
            if normalized_title == book.title.lower():
                return book
            
        return None
    
    def find_books_by_author(self, author):
        author = author.strip().lower()
        books_by_author = []
        
        for book in self.books:
            if book.author.lower() == author:
                books_by_author.append(book)
        
        return books_by_author
    
    def add_book(self, book):
        self.books.append(book)
        return book
    
    def remove_book(self, title):
        book = self.find_book(title)
        
        if book is None:
            return None
        
        self.books.remove(book)
        return book
    
    def checkout_book(self, title):
        book = self.find_book(title)
        
        if book is None:
            return None
        
        if book.checkout() is False:
            return False
        
        return book

    def return_book(self, title):
        book = self.find_book(title)
        
        if book is None:
            return None
        
        if book.return_book() is False:
            return False
        
        return book
    
def is_available(book):
    return not book.checked_out
    
def display_available_books(book_list):
    print("Available for Checkout")
    print("----------------------")
    for book in book_list:
        available = is_available(book)
        if available:
            print(f"{book.title} by {book.author}")
            
def display_checked_out_books(book_list):
    print("Currently Checked Out")
    print("----------------------")
    
    for book in book_list:
        available = is_available(book)
        
        if not available:
            print(f"{book.title} by {book.author}")
            
def count_available_books(book_list):
    available_book_count = 0
    
    for book in book_list:
        if is_available(book):
            available_book_count += 1
            
    return available_book_count

def search_book_by_title(title, library):
    book = library.find_book(title)
    
    if book is None:
        print("Book not found.")
        print()
        return False
    
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    
    if book.checked_out:
        print("Available: No")
    else:
        print("Available: Yes")
        
    return True

def search_book_by_author(author, library):
    books = library.find_books_by_author(author)
    
    if books == []:
        print("No books for this author.")
        print()
        return False
    
    for book in books:
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        
        if book.checked_out:
            print("Available: No")
        else:
            print("Available: Yes")
            
    print()
    return True              
        
def checkout_book(title, library):
    book = library.checkout_book(title)
    
    if book is None:
        print("Book not found.")
        return False
    
    if book is False:
        print("Book is already checked out")
        return False
        
    print(f'Successfully checked out "{book.title}".')
    return True

                 
def return_book(title, library):
    book = library.return_book(title)
    
    if book is None:
        print("Book not found.")
        return False
    
    if book is False:
        print(f"{book.title} was never checked out.")
        return False
    
    print(f'Successfully returned "{book.title}".')
    return True

    
def add_book(title, author, library):
    title = format_name(title)
    author = format_name(author)
    
    book = Book(title, author)
    library.add_book(book)
    
    print(f"{book.title} has been added to catalog.")
    return True

def remove_book(title, library):
    book = library.remove_book(title)
    
    if book is None:
        print("Book not found.")
        return False
    
    print(f"{book.title} has been removed from catalog.")
    return True
