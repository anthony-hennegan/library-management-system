from menus import show_welcome_message, greet_reader
from catalog import (
    display_available_books, 
    display_checked_out_books, 
    count_available_books
)
from utils import format_name, format_response

# State
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
librarian = "Anthony"
available_books = count_available_books(books)
checkout_limit = 3

# Render Section    
show_welcome_message(library_name)
print("") 

reader_name = input("What is your name? ")
reader_name = format_name(reader_name)

greet_reader(reader_name)

print("")
while True:
    view_selection_response = input(
        "Would you like to view our book selection? "
        )

    view_selection_response = format_response(view_selection_response)
    print("")

    if view_selection_response == "yes" or view_selection_response == "y":
        print("Ok, great. Below is our selection.")
        print("")
            
        display_available_books(books)
        print("") 
            
        display_checked_out_books(books)
        print("") 
            
        print(f"We have {available_books} books available for checkout.")
        
        while True:
            requested_books = input(
                "How many books would you like to check out? "
                )
            
            try:
                requested_books = int(format_response(requested_books))
                
                if (
                    requested_books <= available_books 
                    and requested_books <= checkout_limit
                    and requested_books > 0
                ):
                    print("Perfect. Let's get you fixed up.")
                    break
                
                elif requested_books == 0:
                    print("No worries. Have a nice day.")
                    break
                else:
                    print("Number must be within available amount.")
                
            except ValueError:
                print("Please enter a number.")
                
        break
    
    elif view_selection_response == "no" or view_selection_response == "n":
        print("No worries. Have a nice day!")
        break
        
    else:
        print("Please type yes or no.")
    

            

