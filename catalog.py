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
    
    def update_title(self, new_title):
        self.title = new_title
        
        return self
    
    def update_author(self, new_author):
        self.author = new_author
        
        return self
    
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
    
    def remove_book(self, book):
         
        if book is None:
            return None
        
        self.books.remove(book)
        return book
    
    def update_book_title(self, book, new_title):
        new_title = new_title.strip()
        
        if book is None:
            return None
        
        if not new_title:
            return False
        
        return book.update_title(new_title)

    def update_book_author(self, book, new_author):
        new_author = new_author.strip()
        
        if book is None:
            return None
        
        if not new_author:
            return False
        
        return book.update_author(new_author)
        
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
    
    print("     SEARCH RESULTS    ")
    print("-----------------------")
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    
    if book.checked_out:
        print("Available: No")
        print()
    else:
        print("Available: Yes")
        print()
        
    return True

def search_book_by_author(author, library):
    books = library.find_books_by_author(author)
    
    if books == []:
        print("     SEARCH RESULTS    ")
        print("-----------------------")
        print("No books for this author.")
        print()
        return False
    
    for book in books:
        print("     SEARCH RESULTS    ")
        print("-----------------------")
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        
        if book.checked_out:
            print("Available: No")
            print()
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
    print()
    return True

                 
def return_book(title, library):
    book = library.return_book(title)
    
    if book is None:
        print("Book not found.")
        return False
    
    if book is False:
        print("Book is already returned.")
        return False
    
    print(f'Successfully returned "{book.title}".')
    print()
    return True

    
def add_book(title, author, library):
    title = format_name(title)
    author = format_name(author)
    
    book = Book(title, author)
    library.add_book(book)
    
    print(f"{book.title} has been added to catalog.")
    print()
    return True

def remove_book(title, library):
    book = library.find_book(title)

    if book is None:
        print("Book not found.")
        return None
    
    while True:
        print(f"Are you sure you want to delete {book.title}? ")
        confirmation = input("Enter yes or no: ")
        print()
        
        if confirmation.strip().lower() == "yes":
            library.remove_book(book)
            print(f"{book.title} has been removed from catalog.")
            print()
            return True
        elif confirmation.strip().lower() == "no":
            return False
        else:
            print("Please enter yes or no.")
            print()



def update_book_title(library, old_title, new_title):
    old_title = old_title.strip().lower()
    book = library.find_book(old_title)
    
    if book is None:
        print("Book not found.")
        print()
        return None

    old_title = book.title
    updated_book = library.update_book_title(book, new_title)
    
    if updated_book is False:
        print("Invalid Title.")
        print()
        return False
    
    print(f"{old_title} has been changed to {updated_book.title}")
    return True

def update_book_author(library, title, new_author):
    book = library.find_book(title)
    
    if book is None:
        print("Book not found.")
        print()
        return None

    old_author = book.author
    updated_book = library.update_book_author(book, new_author)
    
    if updated_book is False:
        print("Invalid author name.")
        print()
        return False
    
    print(f"{old_author} has been changed to {updated_book.author}")
    print()
    return True