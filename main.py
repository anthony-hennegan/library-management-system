from menus import (
    show_welcome_message, 
    greet_reader,
    show_main_menu
    )
from catalog import (
    display_available_books, 
    display_checked_out_books, 
    count_available_books,
    search_book_by_title,
    checkout_book,
    return_book,
    add_book,
    remove_book
)
from utils import format_name

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
books = [
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "checked_out": True
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "checked_out": False
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "checked_out": False
    }
]

library_name = "Bailey's Books and Bargains"

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
        display_available_books(books)
        print("")
            
        display_checked_out_books(books)
        print("")
    
    elif users_choice == '2':
        search_title = input("Enter book title: ")
        print("")

        search_book_by_title(search_title, books)
        
    elif users_choice == '3':
        checkout_title = input("Which book would you like to checkout? ") 
        print("")
        
        checkout_book(checkout_title, books)

    elif users_choice == '4':
        return_title = input("Which book would you like to return? ") 
        print("")
        
        return_book(return_title, books)
        
    elif users_choice == '5':
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        
        add_book(title, author, books)

    elif users_choice == '6':
        title = input("Enter book title: ")
        
        remove_book(title, books)
             
    elif users_choice == '7':
        print("Thanks for stopping by!")
        break
    
    else:
        print("Please enter a valid option.")
    

        
