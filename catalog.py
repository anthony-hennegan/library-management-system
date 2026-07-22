from utils import format_name

def is_available(book):
    return not book["checked_out"]
    
def display_available_books(book_list):
    print("Available for Checkout")
    print("----------------------")
    for book in book_list:
        available = is_available(book)
        if available:
            print(f"{book['title']} by {book['author']}")
            
def display_checked_out_books(book_list):
    print("Currently Checked Out")
    print("----------------------")
    for book in book_list:
        available = is_available(book)
        if not available:
            print(f"{book['title']} by {book['author']}")
            
def count_available_books(book_list):
    available_book_count = 0
    for book in book_list:
        if is_available(book):
            available_book_count += 1
    return available_book_count

def search_book_by_title(title, book_list):
    title = title.strip().lower()
    found_book = False
    
    for book in book_list:
        if title == book['title'].lower():
            found_book = True
            
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            
            if not book['checked_out']:
                print("Available: Yes")
            else:
                print("Available: No")
                
            break
        
    if not found_book:
        print("Book not found.")
        
def checkout_book(title, book_list):
    title = title.strip().lower()
    found_book = False
    
    #Search for book
    for book in book_list:
        if title == book['title'].lower():
            found_book = True
            
            if not book['checked_out']:
                book["checked_out"] = True
                print(f'Successfully checked out "{book["title"]}".')
            else:
                print("Book is already checked out")
                
            break
 
    if not found_book:
        print("Book not found.")
        
def return_book(title, book_list):
    title = title.strip().lower()
    found_book = False
    
    #search for book
    for book in book_list:
        if title == book['title'].lower():
            found_book = True
            
            if book['checked_out']:
                book['checked_out'] = False
                print(f"{book['title']} has been returned.")
            else:
                print(f"{book['title']} is already returned.")
                
            break
        
    if not found_book:
        print("Book not found.")
    
def add_book(title, author, book_list):
    book_title = format_name(title)
    book_author = format_name(author)
    
    new_book = {
        "title": book_title,
        "author": book_author,
        "checked_out": False
    }
    book_list.append(new_book)
    print(f"{book_title} has been added to catalog.")
    
def remove_book(title, book_list):

    found_book = False
    title = title.strip().lower()
    
    for book in book_list:
        
        if title == book['title'].lower():
            found_book = True
            book_list.remove(book)
            print(f"{book['title']} has been removed from catalog.")
            
            break
    if not found_book:
        print("Book not found.")
    
