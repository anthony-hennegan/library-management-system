from menus import (
    show_welcome_message,
    greet_reader,
    show_menu
    )
from catalog import (
    display_available_books,
    display_checked_out_books,
    search_book_by_title,
    search_book_by_author,
    checkout_book,
    return_book,
    add_book,
    remove_book,
    Library,
    update_book_title,
    update_book_author
)
from utils import format_name
from storage import load_books, save_books
from json import JSONDecodeError


menu_options = [
    "View Books",
    "Search by Title",
    "Search by Author",
    "Check Out Book",
    "Return Book",
    "Add Book",
    "Remove Book",
    "Update Book Title",
    "Update Book Author",
    "Exit"
]

# Load saved data and fall back to an empty library if no valid save exists.
try:
    books = load_books()
except FileNotFoundError:
    print("No saved book data found. Starting with an empty library.")
    books = []
except JSONDecodeError:
    print("Saved book data is empty or invalid. Starting with an empty library.")
    books = []
    
library_name = "Bailey's Books and Bargains"
library = Library(library_name, books)
   

show_welcome_message(library_name)
print("") 

reader_name = format_name(input("What is your name? "))

greet_reader(reader_name)
print("")

# Main application loop. Each completed action returns here until Exit is selected.
while True:
    print()
    print("      MAIN MENU")
    print("----------------------")
    show_menu(menu_options)
    print("")
    
    while True:
        try:
            users_choice = int(input("Enter option number: ").strip())
            print("")
            break
        except ValueError:
            print("Invalid Input")
            print()
            

    if users_choice == menu_options.index("View Books")+1:
        
        display_available_books(library.books)
        print()
            
        display_checked_out_books(library.books)
        print()
   
    
    elif users_choice == menu_options.index("Search by Title")+1:
        search_title = input("Enter book title: ")
        print()

        search_book_by_title(search_title, library)
                
    elif users_choice == menu_options.index("Search by Author")+1:
        search_title = input("Enter author's name: ")
        print()

        search_book_by_author(search_title, library)
        
    elif users_choice == menu_options.index("Check Out Book")+ 1:
        checkout_title = input("Which book would you like to checkout? ") 
        print()
        
        if checkout_book(checkout_title, library):
            save_books(library.books)

    elif users_choice == menu_options.index("Return Book")+1:
        return_title = input("Which book would you like to return? ")
        print()
        
        if return_book(return_title, library):
            save_books(library.books)
        
    elif users_choice == menu_options.index("Add Book")+1:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        print()
        
        if add_book(title, author, library):
            save_books(library.books)

    elif users_choice == menu_options.index("Remove Book")+1:
        title = input("Enter book title: ")
        
        if remove_book(title, library):
            save_books(library.books)
    
    elif users_choice == menu_options.index("Update Book Title")+1:
        title = input("Enter book title: ")
        new_title = input("Enter new title: ")
        print()
        
        if update_book_title(library, title, new_title):
            save_books(library.books)   
               
    elif users_choice == menu_options.index("Update Book Author")+1:
        title = input("Enter book title: ")
        new_author = input("Enter new author: ")
        print()
        
        if update_book_author(library, title, new_author):
            save_books(library.books)   
    
             
    elif users_choice == menu_options.index("Exit")+1:
        print("Thanks for stopping by!")
        break
    
    else:
        print("Please enter a valid option.")
    

        
