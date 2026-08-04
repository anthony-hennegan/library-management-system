from menus import (
    show_welcome_message,
    greet_reader,
    show_main_menu
    )
from catalog import (
    display_available_books,
    display_checked_out_books,
    search_book_by_title,
    checkout_book,
    return_book,
    add_book,
    remove_book,
    Library
)
from utils import format_name
from storage import load_books, save_books


# State
menu_options = [
    "View Books",
    "Search Books",
    "Check Out Book",
    "Return Book",
    "Add Book",
    "Remove Book",
    "Exit"
]

books = load_books()
library_name = "Bailey's Books and Bargains"
library = Library(library_name, books)

# Render Section    

# Greeting
show_welcome_message(library_name)
print("") 

reader_name = format_name(input("What is your name? "))

greet_reader(reader_name)
print("")

# Main Menu
while True:
    show_main_menu(menu_options)
    print("")
    
    users_choice = input("Enter option number: ").strip()
    print("")

    if users_choice == '1':
        display_available_books(library.books)
        print("")
            
        display_checked_out_books(library.books)
        print("")
    
    elif users_choice == '2':
        search_title = input("Enter book title: ")
        print("")

        search_book_by_title(search_title, library)
        
    elif users_choice == '3':
        checkout_title = input("Which book would you like to checkout? ") 
        print("")
        
        if checkout_book(checkout_title, library):
            save_books(library.books)

    elif users_choice == '4':
        return_title = input("Which book would you like to return? ") 
        print("")
        
        if return_book(return_title, library):
            save_books(library.books)
        
    elif users_choice == '5':
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        
        if add_book(title, author, library):
            save_books(library.books)

    elif users_choice == '6':
        title = input("Enter book title: ")
        
        if remove_book(title, library):
            save_books(library.books)
             
    elif users_choice == '7':
        print("Thanks for stopping by!")
        break
    
    else:
        print("Please enter a valid option.")
    

        
