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
book_count = len(books)
is_open = True
checkout_limit = 3

# Logic Functions
def show_welcome_message(name):
    print(f"Welcome to {name}")
    
def greet_reader(name):
    print(f"Hello {name}.")

def format_name(name):
    return name.strip().title()

def format_response(response):
    return response.strip().lower()

def display_books(book_list):
    for book in book_list:
        if book["checked_out"]:
            print(f"- {book['title']} by {book['author']} ---- Unavailable")
        else:
            print(f"- {book['title']} by {book['author']} ---- Available")
            
# Render Section    
show_welcome_message(library_name)

reader_name = input("What is your name? ")
reader_name = format_name(reader_name)

greet_reader(reader_name)

if not is_open:
    print("The library is closed.")

print("")
view_selection_response = input("Would you like to view our book selection? ")
view_selection_response = format_response(view_selection_response)

if view_selection_response == "yes" or view_selection_response == "y":
    print("Ok, great. Below is our selection.")
    print("")
    print("Bailey's Books")
    print("----------------")
    display_books(books)
    
    print("") 
    print(f"We have {book_count} books in our library.")
    requested_books = input("How many books would you like to check out? ")
    requested_books = int(format_response(requested_books))

    if requested_books <= checkout_limit and is_open:
        print("Perfect. Let's get you fixed up.")
    else:
        print("Checkout is not available.")
        
        
elif view_selection_response == "no" or view_selection_response == "n":
    print("No worries. Have a nice day!")
else:
    print("Please type yes or no.")

